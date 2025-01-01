from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

import os
import uvicorn

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

loader = DirectoryLoader('./assets/pdfs/', glob="./*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()
print('Documents Loaded')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=250)
texts = text_splitter.split_documents(docs)
print('Texts Split')

embeddings = HuggingFaceEmbeddings(model_name=os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2"))
db = FAISS.from_documents(texts, embeddings)
print('Database Loaded')

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})

repo_id="HuggingFaceH4/zephyr-7b-beta"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_new_tokens=2048,temperature=0.7)

prompt_template = """
You are FarmFlow, a trusted AI assistant for rice farming. You are designed to provide concise, easy-to-understand answers and practical advice on all aspects of rice farming. Your role is to help farmers make informed decisions that can enhance crop health, increase yield, and reduce costs.

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

You will be provided with context for the given prompt which you will use to tailor your answers.

{context}

Question: {question}

Answer:
"""

PROMPT = PromptTemplate(
 template=prompt_template, input_variables=["context", "question"]
)

retrievalQA = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
print('LLM and Retrieval QA Chain Loaded')

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    try:
        # print(query.question)
        result = retrievalQA.invoke({"query": query.question})
        return {"answer": result['result']}
    except Exception as e:
        print(e)
        if "Model too busy" in str(e):
            return {"answer": "The model is currently overloaded. Please try again later."}
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
