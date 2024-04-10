#!/usr/bin/python3
"""Objects that handle all default Restful API actions for categories"""
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models.category import Category
from models import storage
from api.v1.views import app_views


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
@swag_from('documentation/categories/get_categories.yml', methods=['GET'])
def get_categories():
    """Retrieves the list of all expense objects
    or a specific category
    """
    all_categories = storage.all(Category).values()
    list_categories = []
    for category in all_categories:
        list_categories.append(category.to_dict())
    return jsonify(list_categories)


@app_views.route('/categories/<category_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/categories/get_category.yml', methods=['GET'])
def get_category(category_id):
    """Retrieves a category"""
    category = storage.get(Category, 'id', category_id)
    if not category:
        abort(404)
    return jsonify(category.to_dict())


@app_views.route('/categories/<category_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/categories/delete_category.yml', methods=['DELETE'])
def delete_category(category_id):
    """Deletes a category object"""

    category = storage.get(Category, 'id', category_id)
    if not category:
        abort(404)

    storage.delete(category)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
@swag_from('documentation/categories/post_category.yml', methods=['POST'])
def post_category():
    """Create a Category"""
    if not request.get_json():
        abort(400, "Not a JSON")

    data = request.get_json()
    if not all(key in data for key in ['name']):
        abort(400, "Missing required fields")

    try:
        instance = Category(**data)
        instance.save()
        return make_response(jsonify(instance.to_dict()), 201)
    except Exception as e:
        abort(500, f"Failed to create category: {str(e)}")


@app_views.route('/categories/<category_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/categories/put_category.yml', methods=['PUT'])
def put_category(category_id):
    """Updates a category"""
    category = storage.get(Category, 'id', category_id)

    if not category:
        abort(404)

    if not request.get_json():
        abort(400, "Not a JSON")

    ignore = ['id', 'user_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(category, key, value)
    storage.save()
    return make_response(jsonify(category.to_dict()), 200)
