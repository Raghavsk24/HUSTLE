from flask import Flask, request, render_template
import os
from scanner import process_resume  
app = Flask(__name__)

# Create uploads folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route to Upload File
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"

        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process Resume
        highest_hustle, highest_score = process_resume(file_path)

        if highest_hustle:
            return render_template('results.html', hustle=highest_hustle, score=highest_score) 
        else:
            return "No relevant side hustles found."

    return render_template('upload.html')  

if __name__ == "__main__":
    app.run(debug=True)
