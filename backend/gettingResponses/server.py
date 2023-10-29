from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import json
from flask_cors import CORS
import subprocess
import sys



# Initialize Flask app and set up CORS
app = Flask(__name__)
CORS(app)

# Configuration settings
app.config['UPLOAD_FOLDER'] = './uploads'
VIDEO_FILENAME = 'video.mp4'  # The fixed filename for the uploaded video

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Check if "video.mp4" already exists and delete it
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], VIDEO_FILENAME)):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], VIDEO_FILENAME))
            
            # Save the uploaded file as "video.mp4"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], VIDEO_FILENAME))
            return redirect(url_for('download_file', name=VIDEO_FILENAME))

@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
    try:
        with open('./recommendations.json', 'r') as f:
            recommendations = json.load(f)
        print("API hit, read file successfully", recommendations)  # Debugging line
        return jsonify(recommendations)
    except Exception as e:
        print(f"Error: {e}")  # Debugging line
        return jsonify({"error": "Failed to read recommendations"}), 500


@app.route('/run_gpt_response', methods=['POST'])
def run_gpt_response():
    try:
        # Run gptresponse.py
        subprocess.run([sys.executable, '/Users/sinehanezhilmuthu/Desktop/csShit/stev2/backend/gettingResponses/gptresponse.py'], check=True)
        
        return jsonify({"status": "success"}), 200
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500
    
if __name__ == "__main__":
    app.run()
