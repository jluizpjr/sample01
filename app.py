from flask import Flask, render_template, request
from json2html import *
import os
import sys
import json

host = os.environ.get('HOSTNAME', 'localhost')
env=json.dumps({**{}, **os.environ}, indent=2)


app = Flask(__name__)

@app.route('/')
def index():

    print(env)
    table=json2html.convert(json = env)
    return render_template('index.html',host=host,table=table)
