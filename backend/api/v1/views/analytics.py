#!/usr/bin/pyhton3
"""Statistics and analytics"""
from flask import jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from flasgger import swag_from
from api.v1.views import app_views
from models.user import User



@app_views.route('/analytics', methods=['GET'])
@swag_from('documentation/analytics/get_analytics.yml', methods=['GET'])
@jwt_required()
def get_analytics():
    """Retrieves expense statistics for the authenticated user."""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    total_expenses = sum(expense.amount for expense in current_user.expenses)

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
