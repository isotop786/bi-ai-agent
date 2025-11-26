from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel

class InputData(BaseModel):
    prompt: str

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
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message
    )

    return {
        "reply": response.choices[0].message.content

    }

@app.post("/bi-agent")
async def business_agent(input: InputData):
    # return prompt
    message = [{"role": "user", "content": input.prompt}]
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message
    )

    return {
        "reply": response.choices[0].message.content
    }


