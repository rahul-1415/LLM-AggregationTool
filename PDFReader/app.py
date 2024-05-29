from flask import Flask, render_template
from PyPDF2 import PdfReader
from nltk.tokenize import sent_tokenize
import io

app = Flask(__name__)

pdf_location = "/Users/rahul/Downloads/sentenceRead.pdf"  # Specify your PDF location here

def convert_pdf_to_sentences(pdf_location):
    with open(pdf_location, "rb") as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        sentences = sent_tokenize(text)
        return sentences

sentences = convert_pdf_to_sentences(pdf_location)

@app.route('/')
def home():
    return render_template('sentences.html', sentences=sentences)

if __name__ == '__main__':
    app.run(debug=True)