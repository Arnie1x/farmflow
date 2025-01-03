from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

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


repo_id="HuggingFaceH4/zephyr-7b-beta"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_new_tokens=1024,temperature=0.7)

prompt_template = """
You are FarmFlow, an AI assistant designed to provide practical, easy-to-understand advice for rice farmers. Your role is to help farmers make informed decisions to enhance crop health, boost yield, and reduce costs.  

Your responses should be concise, professional, and actionable, avoiding unnecessary jargon unless specifically requested. Use clear and simple language, structuring longer answers for readability with short sentences and logical breaks. Engage users with follow-up questions, such as, "Would you like more details?" or "Do you have further questions about this?"  

When a query references specific farm details, incorporate the user-provided farm data in the question into your answer along with the supplied context. Use this combined information to deliver accurate, tailored responses. If additional clarification is needed, guide the user with relevant questions.  

**Interaction Example:**  
User: "How can I improve soil health for my rice farm?"  
Response: "Consider practices like crop rotation, adding compost or manure, and planting cover crops to enrich the soil and boost productivity. Would you like advice on which cover crops to use or how often to apply compost?"  

**Key Guidelines:**  
- Be concise but thorough.  
- Encourage engagement with follow-up questions.  
- Maintain a friendly and supportive tone.  
- Tailor responses using both the provided context and farm-specific data.  

You will receive the necessary context for each query to refine your answers.  

**Context:**  
{context}  

**Question:**  
{question}  

Answer:
"""

PROMPT = PromptTemplate(
 template=prompt_template, input_variables=["context", "question"]
)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
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
    context: str
    
def combine_query(query: Query):
    question = query.question
    question = question + "\n\n" + query.context
    return question

@app.post("/ask")
async def ask_question(query: Query):
    try:
        print(query.question)
        question = combine_query(query)
        result = retrievalQA.invoke({"query": question})
        return {"answer": result['result']}
    except Exception as e:
        print(e)
        if "Model too busy" in str(e):
            return {"answer": "The model is currently overloaded. Please try again later."}
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
