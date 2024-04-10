#!/usr/bin/pyhton3
"""Statistics and analytics"""
from flask import jsonify
from flasgger import swag_from
from api.v1.views import app_views
from models import storage
from models.category import Category
from models.expense import Expense


@app_views.route('/analytics', methods=['GET'])
@swag_from('documentation/analytics/get_analytics.yml', methods=['GET'])
def get_analytics():
    """Retrieves total expenses for the authenticated user."""
    all_categories = storage.all(Category).values()
    all_expenses = storage.all(Expense).values()

    # Calculate total expenses for all users
    total_expenses = sum(expense.amount for expense in all_expenses)

    # Calculate expenses by category for all users
    expenses_category = {}
    for category in all_categories:
        category_expenses = [expense.amount for expense in category.expenses]
        expenses_category[category.name] = sum(category_expenses)

    analytics_data = {
        "total_expenses": total_expenses,
        "expense_category": expenses_category
    }

    return jsonify(analytics_data), 200
