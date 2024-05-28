from datetime import datetime
from fastapi import FastAPI

import random
from translators import translate_text

from os import getenv
from dotenv import load_dotenv


app = FastAPI()

BACKEND_URL = getenv("BACKEND_URL")

load_dotenv()
key = getenv("key")


@app.get("/")
def index():
    return {"Hi": "Dmytro", "6 ⭐️": "please 🙏"}


@app.get("/randword")
def get_randword():
    words = ["mama", "mila", "ramu"]
    return random.choice(words)

@app.get("/now")
def get_date():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")



@app.get('/trans/{word}')
def translate_word(word: str):
    translated_word = translate_text(word, translator="google", from_language="uk", to_language="en")
    return {"translation": translated_word}
