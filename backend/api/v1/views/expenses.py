#!/usr/bin/python3
"""Objects that handle all default Restful API actions for expenses"""
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models.expense import Expense
from models import storage
from api.v1.views import app_views


@app_views.route('/expenses', methods=['GET'], strict_slashes=False)
@swag_from('documentation/expenses/get_expenses.yml', methods=['GET'])
def get_expenses():
    """Retrieves the list of all expense objects
    or a specific expense
    """
    all_expenses = storage.all(Expense).values()
    list_expenses = []
    for expense in all_expenses:
        list_expenses.append(expense.to_dict())
    return jsonify(list_expenses)


@app_views.route('/expenses/<expense_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/expenses/get_expense.yml', methods=['GET'])
def get_expense(expense_id):
    """Retrieves an expense"""
    expense = storage.get(Expense, 'expense_id', expense_id)
    if not expense:
        abort(404)
    return jsonify(expense.to_dict())


@app_views.route('/expenses/<expense_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/expenses/delete_expense.yml', methods=['DELETE'])
def delete_expense(expense_id):
    """Deletes an expense object"""

    expense = storage.get(Expense, 'expense_id', expense_id)
    if not expense:
        abort(404)

    storage.delete(expense)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/expenses', methods=['POST'], strict_slashes=False)
@swag_from('documentation/expenses/post_expense.yml', methods=['POST'])
def post_expense():
    """Create an Expense"""
    if not request.get_json():
        abort(400, "Not a JSON")

    data = request.get_json()
    if not all(key in data for key in
               ['amount', 'description', 'category', 'user_id']):
        abort(400, "Missing required fields")

    try:
        instance = Expense(**data)
        instance.save()
        return make_response(jsonify(instance.to_dict()), 201)
    except Exception as e:
        abort(500, f"Failed to create expense: {str(e)}")


@app_views.route('/expenses/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/expenses/put_expense.yml', methods=['PUT'])
def put_expense(user_id):
    """Updates an expense"""
    expense = storage.get(Expense, 'user_id', user_id)

    if not expense:
        abort(404)

    if not request.get_json():
        abort(400, "Not a JSON")

    ignore = ['id', 'user_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(expense, key, value)
    storage.save()
    return make_response(jsonify(expense.to_dict()), 200)
