import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()                                                   # load .env in the order to get properties
open_ai = OpenAI(api_key=os.getenv("OPENAI_API"))               # connect to OpenAI api

def audio_to_text(audio_path: str) -> str: 
    with open(audio_path, "rb") as audio_file:
        transcript = open_ai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def speak_with_llm(text: str) -> str:
    response = open_ai.responses.create(
        model="gpt-5.4-nano",
        input=text)
    return response.output_text