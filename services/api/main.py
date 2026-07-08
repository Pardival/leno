# Création d'une api
# Endpoint : POST notes/ -- POST notes/audio -- GET notes/ 
# GET notes/{id} -- PATCH notes/{id} -- DEL notes/{id} -- GET /notes/search?q=...
#cd services/api && uvicorn main:app --reload --port 8000
import os
from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from core.database import engine, Base
from routes import note_route


Base.metadata.create_all(bind=engine)                           # create database
load_dotenv()                                                   # load .env in the order to get properties
open_ai = OpenAI(api_key=os.getenv("OPENAI_API"))               # connect to OpenAI API
app = FastAPI(title="Leno API")                                 # create FastAPI object for rest service

app.include_router(note_route.router)

@app.get("/")
async def read_root():
    response = open_ai.responses.create(
    model="gpt-5.4-nano",
    input="Write a one-sentence bedtime story about a unicorn.")
    print(response.output_text)
    return response.output_text