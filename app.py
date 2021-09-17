from flask import Flask, render_template, request
from urllib.parse import urlparse
o = urlparse(request.base_url)
host = o.hostname


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',host=host)
