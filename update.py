from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace '<token>' with your actual authorization token
AUTH_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkVyaEpDNzNhUnM3cU5hVjVZZHpTIiwiY29tcGFueV9pZCI6Ijd5Q1Rma2lrcXR2emhkcFRPQ2pjIiwidmVyc2lvbiI6MSwiaWF0IjoxNjk4Njg5NTg0NzA4LCJzdWIiOiIyNzBOQnFaY0hEbWNuVHBta3pjZSJ9.6GgE0WfaZGQkvRjxrd6ahsDM2Gighp6KU3r-dt2iyWk'

@app.route('/', methods=['GET', 'POST'])
def update_contact():
    # Define the API endpoint URL for fetching a specific contact
    url = "https://rest.gohighlevel.com/v1/contacts/rl2Zg6qcHLyHKMKdWwsz"
    
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }
    try:
        # Fetch existing contact details
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        existing_contact = response.json()
        print(existing_contact)
        if request.method == 'POST':
            name = request.form['name']
            phone = request.form['phone']
            email = request.form['email']
            city = request.form['city']
            state = request.form['state']
            postalCode = request.form['postalCode']
            website = request.form['website']
            # Create the data payload for the PUT request
            data = {
                'name': name,
                'phone': phone,
                'email': email,
                'city': city,
                'state': state,
                'postalCode': postalCode,
                'website': website,
                'tags': 'market'
            }
            response = requests.put(url, headers=headers, json=data)
            response.raise_for_status()
            updated_info = response.json()
            return jsonify(updated_info)
        return render_template('update.html', contact=existing_contact)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Error occurred", 500
    
    
# this code for delete contact 
@app.route('/delete', methods=['GET', 'POST'])
def delete_contact():
    url = "https://rest.gohighlevel.com/v1/contacts/rl2Zg6qcHLyHKMKdWwsz"
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return jsonify({'status': 'success', 'message': 'Contact deleted successfully'})
    else:
        return jsonify({'status': 'error', 'message': f'Error deleting contact: {response.text}'})
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)
