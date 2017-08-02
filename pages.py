
from flask import Flask, render_template



DEBUG = True
app = Flask(__name__)

@app.route('/')
def index():
    "render the home page"
    return render_template('index.html')
