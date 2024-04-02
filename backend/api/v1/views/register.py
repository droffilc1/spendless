#!/usr/bin/python3
"""User registration"""
from flask import request, jsonify
from flasgger import swag_from
from werkzeug.security import generate_password_hash
from api.v1.views import app_views
from models.user import User
from models import storage

@app_views.route('/register', methods=['POST'])
@swag_from('documentation/register/post_register.yml', methods=['POST'])
def register():
    """User registration"""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Query the database to check if the username already exists
    existing_user = storage.get(User, 'username', username)
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password)

    # Add the new user to the session and commit transaction
    try:
        storage.new(new_user)
        storage.save()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        storage.rollback()
        return jsonify({'message': 'Error registering user', 'error': str(e)}), 500
    finally:
        storage.close()
