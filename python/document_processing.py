import os
from dotenv import load_dotenv
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from text_loader import TextLoader

load_dotenv()

def load_documents(directory_path):
    print(f"Loading documents from {directory_path}")
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            try:
                loader = TextLoader()
                documents.extend(loader.load_text(os.path.join(directory_path, filename)))
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return documents

def build_vector_store(documents):
    print("Building vector store...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.create_documents(documents)
    split_docs = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name=os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    )
    vector_store = FAISS.from_documents(split_docs, embeddings)
    return vector_store

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def create_qa_chain(vector_store, endpoint_url):
    print("Creating QA chain...")
    retrieval_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    # print(retrieval_prompt)
    template = ChatPromptTemplate([
    ("human", "{inputs}"),
    ])
    
    llm = HuggingFaceEndpoint(
        endpoint_url=endpoint_url,
        max_new_tokens=1024,
        temperature=0.7,
    )
    # Combine documents using the retrieved prompt
    # combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retriever = vector_store.as_retriever()
    # docs = retriever.invoke("rice flour")
    # print("Retrieved documents:", "\n\n".join(doc.page_content for doc in docs))

    # Create the retrieval pipeline
    qa_chain = (
    {
	    "input": RunnablePassthrough(),
	    "context": retriever | format_docs
    }
    | retrieval_prompt
    | llm
    | StrOutputParser()
    )
    return qa_chain
