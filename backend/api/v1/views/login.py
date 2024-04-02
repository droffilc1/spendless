import logging
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from werkzeug.security import check_password_hash
from api.v1.views import app_views
from models.user import User
from models import storage

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app_views.route('/login', methods=['POST'])
@swag_from('documentation/login/post_login.yml', methods=['POST'])
def login():
    """User login"""
    data = request.json
    email = data.get('email')
    password = data.get('password')

    logger.debug('Login attempt for email: %s', email)

    # Retrieve user from database
    try:
        user = storage.get(User, 'email', email)
        logger.debug('User retrieved from the database: %s', user)
    except Exception as e:
        logger.error('Error retrieving user from the database: %s', e)
        return jsonify({'message': 'An error occurred while processing your request'}), 500

    # Check if user exists
    if not user:
        logger.debug('User with email %s not found', email)
        return jsonify({'message': 'User not found'}), 404

    # Log retrieved user
    logger.debug('Retrieved user: %s', user)

    # Verify password
    if not check_password_hash(user.password, password):
        logger.debug('Incorrect password for user %s', email)
        return jsonify({'message': 'Invalid email or password'}), 401

    # Log successful authentication
    logger.debug('User %s authenticated successfully', email)

    # Create JWT token
    access_token = create_access_token(identity=user.id)

    # Return the token to the client
    return jsonify({'access_token': access_token}), 200
