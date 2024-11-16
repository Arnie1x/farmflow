from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from document_processing import load_documents, build_vector_store, create_qa_chain
import uvicorn

# Load resources at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    global qa_chain
    documents = load_documents("assets/converted_texts")
    vector_store = build_vector_store(documents)
    # Specify the desired model from HuggingFace
    qa_chain = create_qa_chain(vector_store, model_name="bert-base-uncased")  # Change this to the model you prefer
    yield
    
# FastAPI app setup
app = FastAPI(lifespan=lifespan)

# Pydantic model for request body
class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    try:
        answer = qa_chain.run(query.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
