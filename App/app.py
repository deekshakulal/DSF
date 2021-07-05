from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/Users/dell/Documents/Final year proj/dsf/App/Files'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/first")
def first():
    import libs
    return "<h1>Home Page</h1>"

@app.route('/addRegion', methods=['POST'])
def addRegion():
    #x=request.form['files']
    fs=[]
    x=request.files.getlist('files')
    import functions
    for f in x:
        fs.append(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    print(fs)
    return(functions.getTriplets(fs))

if __name__ == '__main__':
    app.run(debug=True)