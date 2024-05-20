from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

USERS = {
	"admin": "password123",
	"user1": "mypassword"
}

def check_auth(username, password):
	return USERS.get(username) == password

def authenticate():
	message = {'message': 'Could not verify, login with proper credentials.'}
	response = jsonify(message)
	response.status_code = 401
	response.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
	return response

def decode_auth(auth_header):
	auth_type, auth_string = auth_header.split(' ')
	decoded_bytes = base64.b64decode(auth_string)
	decoded_string = decoded_bytes.decode('utf-8')
	return decoded_string.split(':')


@app.route('/')
def public_route():
	return jsonify(message="Welcome to our Flask App. You are using the public route.")

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

	return jsonify(message="Welcome to our App. You are using the protected route.")


if __name__ == '__main__':
	app.run(debug=True)
