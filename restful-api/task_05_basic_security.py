from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity


)

app = Flask(__name__)

# Configure JWT with a strong secret key
app.config['JWT_SECRET_KEY'] = 'your-very-strong-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user store with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication verification callback
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash
    (users[username]['password'], password):
        return users[username]
    return None


# Endpoint protected with Basic HTTP Authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# Endpoint for JWT login that issues a token upon valid credentials
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Bad username or password"}), 401

    # Create a JWT token including the user's role
    access_token = create_access_token
    (identity={"username": username, "role": user['role']})
    return jsonify(access_token=access_token), 200


# Endpoint protected with JWT token authentication
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Endpoint with role-based protection (admin only)
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Custom JWT error handlers to ensure a 401 status code
@jwt.unauthorized_loader
def unauthorized_response(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_response(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
