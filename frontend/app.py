from flask import Flask, render_template
from os import getenv
from requests import get
from translators import translate_text

app = Flask(__name__)

BACKEND_URL = getenv("BACKEND_URL")

@app.get('/')
def index():
    return render_template("index.html")


@app.get("/randword")
def get_randword():
    url = get(f'{BACKEND_URL}/randword')
    if url.status_code == 200:
        context = {"context" : str(url.json())}
        print(context)
        return render_template("index.html", **context)
    return (f"Error - {url.status_code}")


@app.get('/now')
def time_now():
    url = get(f'{BACKEND_URL}/now')
    if url.status_code == 200:
        context = {"context" :  str(url.json())}
        print(context)
        return render_template("index.html", **context)
    return (f"Error - {url.status_code}")



@app.route('/trans/<word>')
def translate_word(word: str):
    translated_word = translate_text(word, translator="google", from_language="uk", to_language="en")
    context = {"translation": translated_word}
    return render_template("index.html", **context)