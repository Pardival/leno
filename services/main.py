# Création d'une api
# Endpoint : POST notes/ -- POST notes/audio -- GET notes/ 
# GET notes/{id} -- PATCH notes/{id} -- DEL notes/{id} -- GET /notes/search?q=...
#uvicorn main:app --reload --port 8000
import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from core.database import engine, Base

Base.metadata.create_all(bind=engine)                           # create databse
load_dotenv()                                                   # load .env in the order to get properties
open_ai = OpenAI(os.getenv("OPENAI_API"))                       # connect to OpenAI API
app = FastAPI()                                                 # create FastAPI object for rest service    

@app.get("/")
async def read_root():
    response = open_ai.responses.create(
    model="gpt-5.4-nano",
    input="Write a one-sentence bedtime story about a unicorn.")
    print(response.output_text)
    return response.output_text


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("notes/")
async def post_notes():
    return {"post notes"}

app.post("notes/audio")
async def post_notes():
    return {"post audio"}

app.get("notes/")
async def post_notes():
    return {"read notes"}

app.get("notes/{item_id}")
async def read_item():
    return {"read notes item_id"}

app.patch("notes/{item_id}")
async def patch_item():
    return {"patch notes item_id"}

app.delete("notes/{item_id}")
async def delete_item():
    return {"delete notes item_id"}
