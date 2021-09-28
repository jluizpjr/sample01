from flask import Flask, render_template, request
from json2html import *
from kubernetes import client, config
import os
import sys
import json

host = os.environ.get('HOSTNAME', 'localhost')

#env=json.dumps({**{}, **os.environ}, indent=2)
env=json.dumps({**{}, **os.environ}, indent=2)

app = Flask(__name__)

@app.route('/details')
def details():

    print(env)
    
    table=json2html.convert(json = env)
    return render_template('index.html',host=host,table=table)

@app.route('/')
def index():

    print(env)
    table=json2html.convert(json = env) 
    return render_template('index.html',host=host,table=table)

@app.route('/help')
def help():  
    table=json2html.convert(json = env)
    return render_template('help.html',host=host,table=kb())

def kb():
    v1=client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    return ret