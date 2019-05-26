import os
import uuid

from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask_ckeditor import CKEditor, upload_success, upload_fail
from flask_dropzone import Dropzone
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError

from search import searchOne
from ocr import ocrIt
from emotion import detectEmotion

from forms import UploadForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Custom config
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']

app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload_for_ckeditor'

# Flask-Dropzone config
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_MAX_FILE_SIZE'] = 3
app.config['DROPZONE_MAX_FILES'] = 30

@app.route('/')
def hello_world():
    return render_template('index.html', **locals())

@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/uploaded-images')
def show_images():
    return render_template('uploaded.html')

def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

@app.route('/find_face')
def find_face():
    return render_template('find_face.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        filepath = app.config['UPLOAD_PATH'] + '/%s'%filename
        ocr_result = ocrIt(filepath)
        get_emotion = detectEmotion(filepath)
        print(get_emotion)
        result = searchOne(filepath)
        session['filenames'] = [filename]
        if result == "-1":
            result = "人脸无法匹配！"
            return render_template('find_face.html', result="人脸验证失败！" + result, \
                                ocr_result=ocr_result, emotion=get_emotion, filepath=filepath)
        return render_template('find_face.html', result="人脸验证成功！你是" + result, \
                                ocr_result=ocr_result, emotion=get_emotion, filepath=filepath)
        # return redirect(url_for('show_images'))
    return render_template('upload.html', form=form)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/gps')
def gps():
    return render_template('gps.html')

if __name__ == '__main__':
    app.run()