import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
open_ai = OpenAI(os.getenv("OPENAI_API"))

def audio_to_text(audio_path: str) -> str: 
    with open(audio_path, "rb") as audio_file:
        transcript = open_ai.audio.transcriptions.create(
            model="whisper-1",
            file7=audio_file
        )
    return transcript.text

def speak_with_llm(text: str) -> str: 
    response = open_ai.response.create(
        model="gpt-5.4-nano",
    input = text)
    return response.output_text