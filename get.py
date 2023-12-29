from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace '<token>' with your actual authorization token
AUTH_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkVyaEpDNzNhUnM3cU5hVjVZZHpTIiwiY29tcGFueV9pZCI6Ijd5Q1Rma2lrcXR2emhkcFRPQ2pjIiwidmVyc2lvbiI6MSwiaWF0IjoxNjk4Njg5NTg0NzA4LCJzdWIiOiIyNzBOQnFaY0hEbWNuVHBta3pjZSJ9.6GgE0WfaZGQkvRjxrd6ahsDM2Gighp6KU3r-dt2iyWk'

# for get all contact in ghl using python 
@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    url = "https://rest.gohighlevel.com/v1/contacts/"
    
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return jsonify(data)  # Return the data as JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Error occurred", 500
    
@app.route('/', methods=['GET'])
def get_data_by_id():
    contact_id = "rl2Zg6qcHLyHKMKdWwsz"
    url = f"https://rest.gohighlevel.com/v1/contacts/{contact_id}"
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return jsonify(data)  # Return the data as JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Error occurred", 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
