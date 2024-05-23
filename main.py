from typing import List
from fastapi import FastAPI, Query
from fastapi.exceptions import HTTPException
import random
from translators import translate_text

app = FastAPI()


@app.get("/")
def index():
    return {"Hi": "Dmytro", "6 ⭐️": "please 🙏"}


@app.get("/randword")
def get_randword():
    words = ["mama", "mila", "ramu"]
    return random.choice(words)

@app.get("/sum/")
# this is a comment from leonid - url exemple  ->  /sum/?n=3&n=4 
def get_calc(n: List[float] = Query(None)):
    try:
        result = sum(n)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@app.get('/trans/{word}')
def translate_word(word: str):
    translated_word = translate_text(word, translator="google", from_language="uk", to_language="en")
    return {"translation": translated_word}
