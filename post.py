from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace '<token>' with your actual authorization token
AUTH_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkVyaEpDNzNhUnM3cU5hVjVZZHpTIiwiY29tcGFueV9pZCI6Ijd5Q1Rma2lrcXR2emhkcFRPQ2pjIiwidmVyc2lvbiI6MSwiaWF0IjoxNjk4Njg5NTg0NzA4LCJzdWIiOiIyNzBOQnFaY0hEbWNuVHBta3pjZSJ9.6GgE0WfaZGQkvRjxrd6ahsDM2Gighp6KU3r-dt2iyWk'

# for contact POST in ghl
@app.route('/', methods=['GET', 'POST'])
def main():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    postalCode = request.form.get('postalCode')
    website = request.form.get('website')
    # Define the API endpoint URL for creating a contact
    api_url = "https://rest.gohighlevel.com/v1/contacts/"
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'}
    # Create the data payload for the POST request
    data = {
        'name': name,
        'phone': phone,
        'email': email,
        'address':address,
        'city':city,
        'state':state,
        'postalCode': postalCode,
        'website':website,
        'tags':'market'
        }
    response = requests.post(api_url, headers=headers, json=data)
    api_response = response.json()  # Parse the JSON response
    if response.status_code == 200:
    # Check the response content for success or error messages
        api_response = response.json()
        print("API Response:", api_response)
    else:
        # Log the full response for further analysis
        print(f"API request failed with status code {response.status_code}")
        print("Response Content:", response.text)
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)