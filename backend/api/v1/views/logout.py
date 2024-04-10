#!/usr/bin/python3
"""Logout user"""
from flask import jsonify, session
from flask_login import current_user, logout_user
from flasgger import swag_from
from api.v1.views import app_views


@app_views.route('/logout', methods=['POST'])
@swag_from('documentation/logout/logout.yml', methods=['POST'])
def logout():
    """User logout"""
    # Check if the user is logged in
    if not current_user.is_authenticated:
        return jsonify({'message': 'User is not logged in'}), 401

    # Logout the user
    logout_user()

    # Clear the session data
    session.clear()

    return jsonify({'message': 'Logout successful'}), 200
