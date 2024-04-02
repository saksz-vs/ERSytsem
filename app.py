# app.py
from flask import Flask, render_template
import requests
import json
import time

app = Flask(__name__)

def fetch_data():
    url = "https://api.thingspeak.com/channels/2491258/feeds.json?api_key=KYTIOEDA78WNEMIF&results=1"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = fetch_data()
    alcohol_sensor = data['feeds'][0]['field1']
    accident_alert = data['feeds'][0]['field2']
    return json.dumps({'alcohol_sensor': alcohol_sensor, 'accident_alert': accident_alert})

if __name__ == '__main__':
    app.run(debug=True)
