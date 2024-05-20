from flask import Flask, request, jsonify
import base64
import requests

app = Flask(__name__)

def basic_auth(username, password):
    # Encode the username and password in Base64
    credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    
    # Construct the HTTP header with Basic authentication
    headers = {"Authorization": f"Basic {credentials}"}
    
    return headers

def make_api_request(url, headers):
    try:
        # Make a request to the API with the provided headers
        response = requests.get(url, headers=headers)
        
        # Check the response status code
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Access denied"}), 401
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error making request: {e}"}), 500

@app.route('/api', methods=['GET'])
def api():
     # Replace 'username' and 'password' with actual credentials
    username = request.args.get('username')
    password = request.args.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    url = "https://api.example.com/protected/resource"
    headers = basic_auth(username, password)
    
    response = make_api_request(url, headers)
    app.logger.debug("Response from API: %s", response.data)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)

