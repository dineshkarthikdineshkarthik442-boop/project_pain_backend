from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_core import ask_ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Project Pain Backend Running"}

@app.post("/ask")
def ask(data: dict):
    return {"reply": ask_ai(data["prompt"])}
