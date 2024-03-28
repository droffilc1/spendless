#!/usr/bin/python3
"""User registration"""
from flask import request, jsonify
from flasgger import swag_from
from werkzeug.security import generate_password_hash
from api.v1.views import app_views
from models.user import User


@app_views.route('/register', methods=['POST'])
@swag_from('documentation/register/post_register.yml', methods=['POST'])
def register():
    """User registration"""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Hash the passsword before storing it
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)

    # Add the new user to the session and commit transaction
    try:
        new_user.save()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as _:
        return jsonify({'message': 'Error registering user'}), 500
