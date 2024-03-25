#!/usr/bin/python3
"""API endpoints"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User
from models.expense import Expense
from models.category import Category


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status of API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def no_of_objects():
    """Retrieves the number of each objects type"""
    classes = [User, Expense, Category]
    names = ["user", "expense", "category"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
