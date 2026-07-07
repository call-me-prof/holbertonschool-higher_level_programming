#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Setup Rate Limiting using the client's IP address
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

# Hardcoded users dictionary for Basic Authentication
users = {
    "user1": {"username": "user1", "password": "password1", "role": "user"},
    "admin": {"username": "admin", "password": "secretpassword", "role": "admin"}
}

# Helper function to validate Basic Auth headers
def check_auth(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return user
    return None

# Route: Protected Route using Basic Authentication
@app.route('/basic-protected')
def basic_protected():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"error": "Unauthorized"}), 401
        
    return jsonify({"message": "Basic Auth Successful"})

# Route: Protected Route using API Key Authentication
@app.route('/api-key-protected')
def api_key_protected():
    # Retrieve API key from custom header 'X-API-Key'
    api_key = request.headers.get('X-API-Key')
    
    # Expected API key for validation
    if api_key != "secret-api-key":
        return jsonify({"error": "Unauthorized"}), 401
        
    return jsonify({"message": "API Key Auth Successful"})

# Route: Rate-limited route allowing only 5 requests per minute
@app.route('/limited-route')
@limiter.limit("5 per minute")
def limited_route():
    return jsonify({"message": "Request successful"})

# Custom error handler for Rate Limit Exceeded (429 Too Many Requests)
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Too many requests"}), 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
