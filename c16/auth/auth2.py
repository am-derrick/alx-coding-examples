from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Dummy user data with multiple users
USERS = {
    "admin": "password123",
    "user1": "mypassword"
}

def check_auth(username, password):
    """Check if a username and password combination is valid."""
    return USERS.get(username) == password

def authenticate():
    """Send a 401 response that enables basic auth"""
    message = {'message': "Could not verify your access level for that URL.\nYou have to login with proper credentials"}
    response = jsonify(message)
    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    return response

def decode_auth(auth_header):
    """Decode the basic auth header."""
    auth_type, auth_string = auth_header.split(' ')
    decoded_bytes = base64.b64decode(auth_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string.split(':')

@app.route('/')
def public_route():
    return jsonify(message="Welcome to the public route!")

@app.route('/protected')
def protected_route():
    auth = request.headers.get('Authorization')
    if not auth:
        return authenticate()
    
    try:
        username, password = decode_auth(auth)
    except Exception as e:
        return authenticate()
    
    if not check_auth(username, password):
        return authenticate()
    
    return jsonify(message="Welcome to the protected route, {}!".format(username))

if __name__ == '__main__':
    app.run(debug=True)

