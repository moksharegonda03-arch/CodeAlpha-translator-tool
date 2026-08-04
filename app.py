from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text")
        target_lang = request.form.get("lang")

        if text and target_lang:
            translated_text = GoogleTranslator(
                source='auto',
                target=target_lang
            ).translate(text)

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
