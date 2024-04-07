#!/usr/bin/python3
"""Login user"""

from flask import request, jsonify, session
from flask_login import login_user
from flasgger import swag_from
from werkzeug.security import check_password_hash
from api.v1.views import app_views
from models.user import User
from models import storage


@app_views.route('/login', methods=['POST'])
@swag_from('documentation/login/post_login.yml', methods=['POST'])
def login():
    """User login"""
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Retrieve user from database
    try:
        user = storage.get(User, 'email', email)
    except Exception as e:
        return jsonify({
            'message': 'An error occurred while processing your request',
            'error': str(e)}
            ), 500

    # Check if user exists and password is correct
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 404

    # Login the user
    login_user(user)

    # Additional user data in session
    session['user_id'] = user.id

    return jsonify({'message': 'Login sucessfull'}), 200
