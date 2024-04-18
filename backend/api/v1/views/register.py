#!/usr/bin/python3
"""User registration"""

from flask import request, jsonify, session
from flask_login import login_user
from werkzeug.security import generate_password_hash
from flasgger import swag_from
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
        return jsonify(
            {'message': 'Username, email, and password are required'}
            ), 400

    # Check if the email is already registered
    existing_user = storage.get(User, 'email', email)
    if existing_user:
        return jsonify({'message': 'Email already registered'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user instance
    new_user = User(username=username, email=email, password_hash=hashed_password)

    # Add the new user to the database
    try:
        storage.new(new_user)
        storage.save()

        # Log in the user after registration
        login_user(new_user)

        # Store additional user data in the session
        session['user_id'] = new_user.id

        return jsonify(
            {'message': 'User registered and logged in successfully'}
            ), 201
    except Exception as e:
        storage.rollback()
        return jsonify(
            {'message': 'Error registering user', 'error': str(e)}
            ), 500
    finally:
        storage.close()
