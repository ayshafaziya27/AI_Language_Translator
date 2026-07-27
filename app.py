from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

print("Loading Hugging Face model...")

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

print("Model Loaded!")

@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""

    if request.method == "POST":

        text = request.form["text"]

        result = translator(text)

        translated_text = result[0]["translation_text"]

    return render_template(
        "index.html",
        translated_text=translated_text
    )

if __name__ == "__main__":
    app.run(debug=True)