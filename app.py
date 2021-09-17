from flask import Flask, render_template
import longhorn

longhorn_url = 'http://127.0.0.1:8080/v1'

client = longhorn.Client(url=longhorn_url)

# Volume operations
# List all volumes
volumes = client.list_volume()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
