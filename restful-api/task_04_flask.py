#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users (Empty by default for the checker)
users = {}

# Route: Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route: Get all usernames stored in the API
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Route: Check API status
@app.route('/status')
def status():
    return "OK"

# Route: Get a specific user object by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route: Add a new user via POST request
@app.route('/add_user', methods=['POST'])
def add_user():
    # Handle invalid or missing JSON body
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get('username')
    
    # Validate that username is provided
    if not username:
        return jsonify({"error": "Username is required"}), 400
        
    # Validate that username doesn't already exist
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # Add user to the in-memory dictionary
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    # Return success response
    response = {
        "message": "User added",
        "user": users[username]
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
