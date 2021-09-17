from flask import Flask, render_template, request
import os
import sys
import json

host = os.environ.get('HOSTNAME', 'localhost')



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',host=host,env=json.dumps({**{}, **os.environ}, indent=2))
