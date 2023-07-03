from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/gps-data', methods=['POST'])
def receive_gps_data():
    data = request.get_json()
    # Process the GPS data here
    print('Received GPS data:', data)
    # You can store it in a database or perform any required actions
    return 'GPS data received successfully'

 