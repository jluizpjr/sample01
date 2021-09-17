from flask import Flask, render_template, request
import os
import sys
import json
import pandas as pd

host = os.environ.get('HOSTNAME', 'localhost')
env=json.dumps({**{}, **os.environ}, indent=2)


app = Flask(__name__)

@app.route('/')
def index():


#    data_dic = {
#        'id': [100, 101, 102],
#        'color': ['red', 'blue', 'red']}

    data_dic = json.dumps({**{}, **os.environ}, indent=2)

    columns = ['key', 'vlue']
    index = ['a', 'b', 'c']

#    df = pd.DataFrame(data_dic, columns=columns, index=index)
    df = pd.DataFrame.from_dict(data_dic,columns=columns, index=index)
    table = df.to_html(index=False)

    return render_template('index.html',host=host,table=table)
