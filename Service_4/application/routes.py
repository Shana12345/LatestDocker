from application import app
import requests


@app.route('/randomName', methods=['GET'])
def sentence():
    beginning = requests.get('http://service_2:5001/randomFS')
    ending = requests.get('http://service_3:5002/randomFS')
    response = beginning.text + " " + ending.text
    return response