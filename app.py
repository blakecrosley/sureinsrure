from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set upload folder path (adjust if needed)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/upload_process', methods=['POST'])
def upload_process():
    if 'declarations_file' not in request.files:
        return "No file part", 400
    file = request.files['declarations_file']
    if file.filename == '':
        return "No selected file", 400

    # Save the file to our uploads folder
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # For now, just confirm it was saved.
    return f"File {file.filename} uploaded successfully!"