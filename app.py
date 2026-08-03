from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    target = data.get("target")

    if not text:
        return jsonify({"translated_text": "Please enter text"})

    try:
        result = GoogleTranslator(source='auto', target=target).translate(text)
        return jsonify({"translated_text": result})
    except Exception as e:
        return jsonify({"translated_text": "Error: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)