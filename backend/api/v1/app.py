#!/usr/bin/python3
"""Entry point for the Flask app"""

from os import getenv
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from models import storage
from models.user import User
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.secret_key = 'SECRET_KEY'
login_manager = LoginManager(app)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/')
def index():
    "Home page test"
    return 'Hello World!'


@app.teardown_appcontext
def close_db(error):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 Error
    ___
    responses:
        404:
            description: a resource was not found
    """
    return make_response(jsonify({"error": "Not found"}), 404)

@login_manager.user_loader
def loader(user_id):
    """Load users from the database"""
    return storage.get(User, 'user_id', user_id)


app.config['SWAGGER'] = {
    'title': 'Spendless RESTful API'
}
Swagger(app)

JWTManager(app)


if __name__ == "__main__":
    host = getenv('API_HOST')
    port = getenv('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
