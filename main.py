from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=openai_api_key)

app = FastAPI()

@app.get("/")
async def hello():
    return "Hello..."


@app.post("/agent")
async def agent(prompt: str):
    message=[{"role":"user","content": prompt}]



