#!/usr/bin/env python3
"""
A simple Flask API.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users.
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Return the API status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return full user data for the given username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the API."""
    new_user = request.get_json()
    if not new_user or 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user['username']
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == '__main__':
    app.run()
