from flask import Flask, render_template, request
from model import img_input
import os
# from PIL import Image

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    imagefile = request.files.get('image')
    full_name = os.path.join('static','files', imagefile.filename)
    imagefile.save(full_name)
    result = str(img_input(full_name))
    im_shot = '/static/files/'+imagefile.filename

    return render_template('index_2.html', result = result, im_shot = im_shot)


if __name__ == "__main__":
    app.run(debug = True)