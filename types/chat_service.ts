import { Client } from "@gradio/client";

class ChatService {
  private gradioClient: any;
  private client: any;
  private systemMessage: string;
  private chatId: string;
  private userId: string;
  
  public messages: any;
  
  constructor() {
    this.init();
    this.client = useSupabaseClient();
    this.userId = useSupabaseUser().value?.id ?? '';
    this.chatId = '';
    this.messages = [];
    this.systemMessage = `
    Welcome to FarmFlow, your trusted AI assistant for rice farming. This chatbot is designed to provide concise, easy-to-understand answers and practical advice on all aspects of rice farming. Your role is to help farmers make informed decisions that can enhance crop health, increase yield, and reduce costs.
    
    When interacting with the user, keep your language simple, professional, and friendly. Your responses should be informative and actionable, avoiding technical jargon or overly complex explanations unless specifically requested by the user. Ensure that your answers are clear and to the point, without excessive detail that may overwhelm the user. 
    
    For longer responses, structure the content so that it is easily readable, using brief sentences and logical breaks. Engage the user with follow-up questions or hints that invite them to ask for more details if needed. For example, you can use phrases like, "Would you like to know more about this?", "Do you need more details on this process?", or "Please let me know if you have any other questions."
    
    Make sure your replies encourage an ongoing conversation by being approachable and supportive. If a user asks a question that requires context or further clarification, respond in a way that helps them elaborate or guide them with a related question.
    
    **Example interaction style**:
    User: "How do I improve soil health for my rice crop?"
    Response: "To improve soil health, consider crop rotation, adding organic matter such as compost, and using cover crops. These practices can enrich the soil and boost productivity. Would you like to know which cover crops work best or how often to apply compost?"
    
    **Key interaction principles**:
    - Be concise but thorough.
    - Encourage user engagement with questions or hints for more information.
    - Maintain an easy-to-follow and conversational tone.
    - Provide detailed answers upon request without overwhelming the user in your initial response.
    
    Remember, your primary goal is to assist rice farmers effectively and ensure they have the knowledge they need to make confident, well-informed decisions. Adjust your tone to be friendly, supportive, and informative, always keeping the user's needs at the forefront.
    `;
  }
  
  private async init() {
    try {
      
      this.gradioClient = await Client.connect("arnie1x/farmflow", {hf_token: useRuntimeConfig().public.huggingFaceApiToken});
    } catch (error) {
      console.error("Error connecting to the Gradio client:", error);
      throw new Error("Gradio client initialization failed");
    }
  }
  
  hasChatID(): boolean {
    if (this.chatId === '') {
      return false;
    } else {
      return true;
    }
  }
  public async sendMessage(userMessage: string): Promise<void> {
    try {
      // Create user message in the database but do not commit until AI response is confirmed
      const newMessage = {
        chat_id: this.chatId,
        user_id: this.userId,
        message: userMessage,
        is_user: true,
        created_at: new Date(),
        updated_at: new Date(),
      };
      // this.messages.push(newMessage);

      // Send the message to the Gradio app
      const result = await this.gradioClient.predict("/chat", {
        message: userMessage,
        system_message: this.systemMessage,
        max_tokens: 512,
        temperature: 0.7,
        top_p: 0.95,
      });
      
      const aiResponse = result.data[0];

      // Store the AI response in the database
      const aiMessage = {
        chat_id: this.chatId,
        user_id: this.userId,
        message: aiResponse,
        is_user: false,
        created_at: new Date(),
        updated_at: new Date(),
      };
      // this.messages.push(aiMessage);
      
      const { data, error: storeError } = await this.client.from("messages").insert([newMessage, aiMessage]).select();
      
      this.messages.push(data[0]);
      this.messages.push(data[1]);

      if (storeError) {
        throw storeError;
      }


    } catch (error) {
      console.error("Error sending or storing the message:", error);
      throw new Error("Message processing failed");
    }
  }

  public async getAllMessages(): Promise<any> {
    try {
      const { data, error: dataError } = await this.client.from("messages").select("*").eq("chat_id", this.chatId);
      if (dataError) {
        throw dataError;
      }
      this.messages = data;
      return data;
    } catch (error) {
      console.error("Error getting messages:", error);
      throw new Error("Message retrieval failed");
    }
  }

  public async setChatId(chatId: string) {
    this.chatId = chatId;
  }

  public async getAllChats(): Promise<any> {
    try {
      const { data, error: dataError } = await this.client.from("chats").select("*").order('updated_at', { ascending: false });

      if (dataError) {
        throw dataError;
      }

      return data;
    } catch (error) {
      console.error("Error getting chats:", error);
      throw new Error("Chat retrieval failed");
    }
  }

  public async createChat(userMessage: string): Promise<string> {
    const customSystemMessage = `
    Your role is to create a concise and appropriate title for each chat session based on the user's initial message. The title should capture the main idea or topic of the prompt in a clear and general way. Keep the titles short (ideally 3-6 words) and relevant to the content of the user's question or statement.

    When generating a title, focus on summarizing the main subject or theme without being too specific. For example, if the first user message is "What fertilizers should I use for better rice yield?", an appropriate title could be "Fertilizer Recommendations" or "Improving Rice Yield".

    Ensure the title is informative and straightforward so users can easily identify the topic of the conversation. Avoid overly technical terms or complex language. Your goal is to create titles that help users quickly understand what the chat is about at a glance.

    **Example guidelines**:
    - Original message: "How do I control pests in my rice field?"
      Generated title: "Pest Control Tips"
    - Original message: "Can you tell me about optimal planting times?"
      Generated title: "Optimal Planting Times"
    - Original message: "What are the best practices for soil preparation?"
      Generated title: "Soil Preparation Practices"

    Keep your titles user-friendly and relevant to the initial question or statement.

    Only return your chosen title and nothing else.
    `;
    try {
      const result = await this.gradioClient.predict("/chat", {
        message: userMessage,
        system_message: customSystemMessage,
        max_tokens: 512,
        temperature: 0.4,
        top_p: 0.95,
      });

      const title = result.data[0];

      const { data, error: chatError } = await this.client.from("chats").insert({ user_id: userId, title: title }).select();

      if (chatError) {
        throw chatError;
      }
      return data[0].id;
    } catch (error) {
      console.error("Error creating new chat:", error);
      throw new Error("Failed to create new chat");
    }
  }
}

export default ChatService;
