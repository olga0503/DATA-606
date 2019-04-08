#!flask/bin/python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

#shows "Hello, World!" on the home page
@app.route('/')
def index():
    return "Hello, World!"


#returns tree Census data in json format on /module5 webpage
@app.route('/module5', methods=['GET'])
def get_tasks():
     uri = "https://data.cityofnewyork.us/resource/uvpi-gqnh.json"
     uResponse = requests.get(uri)
     Jresponse = uResponse.text
     return jsonify(Jresponse)

if __name__ == '__main__':
    app.run(debug=True)