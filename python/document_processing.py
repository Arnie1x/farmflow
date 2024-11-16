import os
from dotenv import load_dotenv

load_dotenv()

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import VectorDBQA
from langchain_community.llms import HuggingFaceHub
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
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(split_docs, embeddings)
    return vector_store

# Function to create a Langchain QA chain using HuggingFaceHub
def create_qa_chain(vector_store, model_name="gpt2"):
    # Create an LLM instance from HuggingFaceHub using the model name
    llm = HuggingFaceHub(repo_id=model_name, model_kwargs={"temperature": 0.7})
    
    # Create a VectorDBQA chain using the provided LLM
    qa_chain = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=vector_store)
    return qa_chain
