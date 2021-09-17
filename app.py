from flask import Flask, render_template, request
import os
import sys

host = os.environ.get('HOSTNAME', 'localhost')



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',host=host,env=os.environ)
