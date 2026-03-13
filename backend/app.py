from flask import Flask, request, send_file, render_template
import os
import PyPDF2

from summarizer import summarize_text
from slide_builder import generate_ppt
from chart_generator import generate_chart_from_text

app = Flask(
    __name__,
    template_folder="../frontend"
)

UPLOAD_FOLDER = "../uploads"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    text = ""

    with open(filepath, "rb") as pdf_file:

        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    slides = summarize_text(text)

    chart = generate_chart_from_text(text)

    ppt_file = generate_ppt(slides, chart)

    return send_file(ppt_file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)