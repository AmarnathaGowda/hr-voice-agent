from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title = "HR Voice Agent")

@app.get("/health")
async def health_check():
    return {"status": "OK", "version": "0.1"}