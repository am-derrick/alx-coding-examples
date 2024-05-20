from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Dummy user data
USERS = {
    "admin": "password123"
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

@app.route('/')
def public_route():
    return jsonify(message="Welcome to the public route!")

@app.route('/protected')
def protected_route():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return jsonify(message="Welcome to the protected route, {}!".format(auth.username))

if __name__ == '__main__':
    app.run(debug=True)

