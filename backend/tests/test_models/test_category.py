#!/usr/bin/python3
"""Test BaseModel for expected behavior"""
import unittest
from models.category import Category
import models


class TestCategory(unittest.TestCase):
    """Test the Category class"""

    def test_is_subclass(self):
        """Test that Category is a subclass of BaseModel"""
        category = Category()
        self.assertIsInstance(category, models.base_model.BaseModel)
        self.assertTrue(hasattr(category, "id"))
        self.assertTrue(hasattr(category, "created_at"))
        self.assertTrue(hasattr(category, "updated_at"))

    def test_name_attr(self):
        """Test that Category has attr name, and it's of type string"""
        category = Category()
        self.assertTrue(hasattr(category, "name"))
        self.assertIsInstance(category.name, str)

    def test_expenses_relationship(self):
        """Test that Category has a relationship with Expense"""
        category = Category()
        self.assertTrue(hasattr(category, "expenses"))
        self.assertIsInstance(category.expenses, list)
        self.assertEqual(category.expenses, [])

    def test_table_name(self):
        """Test that the table name for Category is correct"""
        category = Category()
        self.assertTrue(hasattr(category, "__tablename__"))
        self.assertEqual(category.__tablename__, 'categories')
