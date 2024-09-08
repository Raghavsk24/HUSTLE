# Bug somewhere in the code that prevents file upload as a .pdf and as a .DOCX file.

from flask import Flask, request, render_template, jsonify
import spacy
import PyPDF2
import docx
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

nlp = spacy.load("en_core_web_lg")

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return str(e)

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        return str(e)

def extract_keywords(text):
    doc = nlp(text.lower())
    words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    entities = [ent.text for ent in doc.ents]
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    keywords = list(set(words + entities + noun_chunks))
    return keywords

def calculate_matching_score(resume_keywords, job_keywords):
    matching_keywords = set(resume_keywords) & set(job_keywords)
    if not job_keywords:
        return 0.0
    score = len(matching_keywords) / len(job_keywords)
    return score

def process_resume(resume_file, job_keywords):
    file_extension = os.path.splitext(resume_file)[1].lower()
    if file_extension == ".pdf":
        resume_text = extract_text_from_pdf(resume_file)
    elif file_extension == ".docx":
        resume_text = extract_text_from_docx(resume_file)
    else:
        return None, None

    if resume_text:
        resume_keywords = extract_keywords(resume_text)
        matching_score = calculate_matching_score(resume_keywords, job_keywords)
        return matching_score, resume_keywords
    else:
        return None, None

def download_job_description(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            requirements_section = None
            for header in soup.find_all(["h2", "h3", "h4", "h5", "h6"]):
                if "requirements" in header.text.lower() or "qualifications" in header.text.lower():
                    requirements_section = header.find_next("ul")
                    break

            if requirements_section:
                requirements_text = " ".join(
                    [li.text for li in requirements_section.find_all("li")])
                return requirements_text
            else:
                webpage_text = soup.get_text()
                return webpage_text
        else:
            return None
    except Exception as e:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    job_url = request.form['job_url']
    resume_file = request.files['resume_file']

    job_description = download_job_description(job_url)
    if job_description:
        job_keywords = extract_keywords(job_description)
        matching_score, resume_keywords = process_resume(resume_file, job_keywords)
        if matching_score is not None:
            return jsonify({
                'matching_score': matching_score,
                'resume_keywords': resume_keywords,
                'job_keywords': job_keywords,
                'matching_keywords': list(set(resume_keywords) & set(job_keywords))
            })
    return jsonify({'error': 'Failed to process the resume or job description.'})

if __name__ == "__main__":
    app.run(debug=True)
