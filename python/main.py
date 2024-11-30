from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from document_processing import load_documents, build_vector_store, create_qa_chain
import uvicorn

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Dependency for the QA chain
async def get_qa_chain():
    try:
        documents = load_documents("assets/converted_texts")
        vector_store = build_vector_store(documents)
        qa_chain = create_qa_chain(
            vector_store,
            endpoint_url="https://api-inference.huggingface.co/models/distilbert-base-uncased",
        )
        return qa_chain
    except Exception as e:
        raise RuntimeError(f"Error initializing QA chain: {e}")

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query, qa_chain=Depends(get_qa_chain)):
    try:
        answer = qa_chain.invoke({"input": query.question})
        return {"answer": answer["output"]}
    except Exception as e:
        print(e)
        if "Model too busy" in str(e):
            return {"answer": "The model is currently overloaded. Please try again later."}
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
