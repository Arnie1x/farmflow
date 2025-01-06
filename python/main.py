from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from huggingface_hub import InferenceClient

import os
import uvicorn

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
# Configure CORS
origins = [
    "http://localhost:3000",  # Allow requests from the Nuxt app
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

loader = DirectoryLoader('./assets/pdfs/', glob="./*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()
print('Documents Loaded')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=250)
texts = text_splitter.split_documents(docs)
print('Texts Split')

embeddings = HuggingFaceEmbeddings(model_name=os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2"))
db = FAISS.from_documents(texts, embeddings)
print('Database Loaded')


chat_system_message = """
Welcome to FarmFlow, your trusted AI assistant for rice farming. This chatbot is designed to provide concise, easy-to-understand answers and practical advice on all aspects of rice farming. Your role is to help farmers make informed decisions that can enhance crop health, increase yield, and reduce costs.

When interacting with the user, keep your language simple, professional, and friendly. Your responses should be informative and actionable, avoiding technical jargon or overly complex explanations unless specifically requested by the user. Ensure that your answers are clear and to the point, without excessive detail that may overwhelm the user. 

For longer responses, structure the content so that it is easily readable, using brief sentences and logical breaks. Engage the user with follow-up questions or hints that invite them to ask for more details if needed. For example, you can use phrases like, "Would you like to know more about this?", "Do you need more details on this process?", or "Please let me know if you have any other questions."

When a query references specific farm details, incorporate the user-provided farm data in the question into your answer along with the supplied context. Use this combined information to deliver accurate, tailored responses.

Make sure your replies encourage an ongoing conversation by being approachable and supportive. If a user asks a question that requires context or further clarification, respond in a way that helps them elaborate or guide them with a related question.

**Example interaction style**:
User: "How do I improve soil health for my rice crop?"
Response: "To improve soil health, consider crop rotation, adding organic matter such as compost, and using cover crops. These practices can enrich the soil and boost productivity. Would you like to know which cover crops work best or how often to apply compost?"

**Key interaction principles**:
- Be concise but thorough.
- Encourage user engagement with questions or hints for more information.
- Maintain an easy-to-follow and conversational tone.
- Provide detailed answers upon request without overwhelming the user in your initial response.

You will receive the necessary context for each query to refine your answers.

Remember, your primary goal is to assist rice farmers effectively and ensure they have the knowledge they need to make confident, well-informed decisions. Adjust your tone to be friendly, supportive, and informative, always keeping the user's needs at the forefront.
"""

summary_system_message = """
You are FarmFlow, a trusted AI assistant for rice farming. 
You are designed to provide concise, easy-to-understand answers and practical advice on all aspects of rice farming. 
Your role is to help farmers make informed decisions that can enhance crop health, increase yield, and reduce costs.
You will receive information about a farm, including its name, location, farm activities/events, and weather data such as current temperature and the forecast for the next few hours. 
Summarize this information into one short, easy-to-understand paragraph for the farmer. 
Use the Farm Activities and Weather Data to provide insights and recommendations for the farmer and find any relations/critique between the activities carried out and the weather.
Your response should be concise yet insightful, highlighting any patterns or anomalies in the weather that may impact farm activities. 
Use clear, farmer-friendly language and focus on actionable insights if possible.
"""

title_system_message = """
Your role is to create a concise and appropriate title for each chat session based on the user's initial message. The title should capture the main idea or topic of the prompt in a clear and general way. Keep the titles short (ideally 4-6 words) and relevant to the content of the user's question or statement.

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
"""


retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
print('Retriever Loaded')

class ChatQuery(BaseModel):
    question: str
    context: str
    messages: list
    
    def combine_query_context(self):
        return self.question + "\n\n" + self.context

class SummaryQuery(BaseModel):
    message: str

class TitleQuery(BaseModel):
    question: str
    
def combine_query(query: ChatQuery):
    question = query.question
    question = question + "\n\n" + query.context
    return question

model="Qwen/Qwen2.5-Coder-32B-Instruct"
client = InferenceClient(api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

def get_documents_system_message(documents):
    return {"role": "system", "content": "Use this rice information below extracted from Rice Manuals to enhance your response: \n\n" + documents[0].page_content + "\n" + documents[1].page_content + "\n" + documents[2].page_content}

@app.post("/ask")
async def ask_question(query: ChatQuery):
    try:
        print("Processing query...")
        
        messages = [
            { "role": "system", "content": chat_system_message },
        ]
        
        for message in query.messages:
            messages.append({
                "role": "user" if message["is_user"] else "assistant",
                "content": message["message"]
            })
            
        question = query.combine_query_context()
        documents = retriever.invoke(question)        
        messages.append(get_documents_system_message(documents))
        messages.append({"role": "user", "content": question})

        
        completion = client.chat.completions.create(
            model=model, 
            messages=messages, 
            temperature=0.7,
            max_tokens=1024,
            top_p=0.7
        )
        return {"answer": completion.choices[0].message.content}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")
    
@app.post("/generate-summary")
async def generate_summary(query: SummaryQuery):
    try:
        messages = [
            { "role": "system", "content": summary_system_message },
        ]
        
        documents = retriever.invoke(query.message)
        messages.append(get_documents_system_message(documents))
        messages.append({"role": "user", "content": query.message})
        
        completion = client.chat.completions.create(
            model=model, 
            messages=messages, 
            temperature=0.5,
            max_tokens=512,
            top_p=0.7
        )
        return {"answer": completion.choices[0].message.content}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")
    
@app.post("/generate-title")
async def generate_title(query: TitleQuery):
    try:
        messages = [
            { "role": "system", "content": title_system_message },
        ]
        # documents = retriever.invoke(query.message)
        # messages.append(get_documents_system_message(documents))
        messages.append({"role": "user", "content": query.question})
        
        completion = client.chat.completions.create(
            model=model, 
            messages=messages, 
            temperature=0.5,
            max_tokens=512,
            top_p=0.7
        )
        return {"answer": completion.choices[0].message.content}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
