from flask import Flask, request, render_template, jsonify
import requests
from requests.auth import HTTPBasicAuth
import base64
import datetime
import json

app = Flask(__name__)

# M-Pesa credentials
consumer_key = 'wcGAF3zL5AW6G1NzGyujPdUEpgILusyd'
consumer_secret = 'PAvg9opBE85MkR9Q'
shortcode = '174379'
passkey = 'bfb279f9aa9bbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c9e1a'
callback_url = 'https://dine.keshowins.com/mpesa/callback.html'


def generate_oauth_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = response.json()
    return json_response['access_token']


def generate_password():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data_to_encode = shortcode + passkey + timestamp
    encoded_string = base64.b64encode(data_to_encode.encode())
    return encoded_string.decode('utf-8'), timestamp


def stk_push_request(phone_number, amount):
    access_token = generate_oauth_token()
    password, timestamp = generate_password()
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": "Bearer " + access_token
    }
    payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNzI0MTgwODU2",
    "Timestamp": "20240724180856",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount,
    "PartyA": 254708374149,
    "PartyB": 174379,
    "PhoneNumber": phone_number,
    "CallBackURL": callback_url,
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    phone_number = data['phone']
    amount = data['amount']
    response = stk_push_request(phone_number, amount)

    # Log the transaction (for simplicity, we save to a file here. In a real app, save to a database)
    with open('transactions.log', 'a') as log_file:
        log_file.write(json.dumps(response) + '\n')

    return jsonify(response)


@app.route('/mpesa/callback', methods=['POST'])
def mpesa_callback():
    data = request.json
    # Log the callback data (for simplicity, we print it here. In a real app, save to database)
    print(data)
    with open('callback.log', 'a') as log_file:
        log_file.write(json.dumps(data) + '\n')
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})


if __name__ == '__main__':
    app.run(debug=True)
