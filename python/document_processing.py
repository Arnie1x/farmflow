import os
from dotenv import load_dotenv

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import VectorDBQA
# from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from text_loader import TextLoader

# Function to load and preprocess text files (same as before)
def load_documents(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            loader = TextLoader()
            documents.extend(loader.load_text(os.path.join(directory_path, filename)))
    return documents

# Function to build the vector store from documents (same as before)
def build_vector_store(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.create_documents(documents)
    split_docs = text_splitter.split_documents(docs)
    
    # Using OpenAI embeddings (replace with your choice of embeddings if needed)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(split_docs, embeddings)
    return vector_store

# Function to create a Langchain QA chain using HuggingFaceHub
def create_qa_chain(vector_store, endpoint_url, api_key, model_name="gpt2"):
    # Create an LLM instance from HuggingFaceHub using the model name
    # llm = HuggingFaceHub(repo_id=model_name, model_kwargs={"temperature": 0.7})
    llm = HuggingFaceEndpoint(endpoint_url=endpoint_url, api_key=api_key, model_kwargs={"temperature": 0.7})
    
    # Create a VectorDBQA chain using the provided LLM
    qa_chain = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=vector_store)
    return qa_chain
