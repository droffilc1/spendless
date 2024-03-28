#!/usr/bin/python3
"""User login"""
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from werkzeug.security import check_password_hash
from api.v1.views import app_views
from models.user import User


@app_views.route('/login', methods=['POST'])
@swag_from('documentation/login/post_login.yml', methods=['POST'])
def login():
    """User login"""
    data = request.json
    username = data.get('username')
    passsword = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, passsword):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Create JWT token
    access_token = create_access_token(identity=user.id)
    # Return the token to the client
    return jsonify({'access_token': access_token}), 200
