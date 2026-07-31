from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        try:
            translated_text = GoogleTranslator(source=source, target=target).translate(text)
        except Exception as e:
            translated_text = "Error: " + str(e)

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
 app.run(debug=True, host="0.0.0.0")