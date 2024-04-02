#!/usr/bin/pyhton3
"""Statistics and analytics"""
from flask import jsonify
from flask_login import current_user
from flasgger import swag_from
from api.v1.views import app_views
from models.user import User
from models import storage


@app_views.route('/analytics', methods=['GET'])
@swag_from('documentation/analytics/get_analytics.yml', methods=['GET'])
def get_analytics():
    """Retrieves expense statistics for the authenticated user."""
    user_id = current_user.get_id()
    user = storage.get(User, 'id', user_id)

    if user is None:
        return jsonify({"message": "User not found"}), 404

    total_expenses = sum(expense.amount for expense in user.expenses)

    expenses_category = {}
    for expense in current_user.expenses:
        category_name = expense.category.name
        expenses_category.setdefault(category_name, 0)
        expenses_category[category_name] += expense.amount

    analytics_data = {
        "total_expenses": total_expenses,
        "expense_category": expenses_category
    }

    return jsonify(analytics_data), 200
