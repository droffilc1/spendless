#!/usr/bin/python3
"""Logout user"""
from flask import jsonify, request
from flask_login import current_user, logout_user
from flasgger import swag_from
from api.v1.views import app_views


@app_views.route('/logout', methods=['OPTIONS', 'POST'])
@swag_from('documentation/logout/logout.yml', methods=['POST', 'OPTIONS'])
def logout():
    """Logout user"""
    if request.method == 'OPTIONS':
        # Respond to preflight request
        response = jsonify({})
        response.headers.add(
            'Access-Control-Allow-Origin', 'http://127.0.0.1:5173')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    elif current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logged out successfully'}), 200
    else:
        return jsonify({'message': 'User not logged in'}), 401
