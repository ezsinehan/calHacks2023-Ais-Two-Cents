import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
VIDEO_FILENAME = 'video.mp4'  # The fixed filename for the uploaded video

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
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
