from flask import Flask, send_from_directory
import os

app = Flask(__name__)
BASEDIR = os.getcwd()


@app.route('/')
def index():
    return send_from_directory(BASEDIR, 'index.html')


@app.route('/<string:filename>')
def content(filename):
    return send_from_directory(BASEDIR, filename)


if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0')
