#!/usr/bin/python3
"""Test BaseModel for expected behavior"""

import unittest
from models.expense import Expense
import models


class TestExpense(unittest.TestCase):
    """Test the Expense class"""

    def test_is_subclass(self):
        """Test that Expense is a subclass of BaseModel"""
        expense = Expense()
        self.assertIsInstance(expense, models.base_model.BaseModel)
        self.assertTrue(hasattr(expense, "id"))
        self.assertTrue(hasattr(expense, "created_at"))
        self.assertTrue(hasattr(expense, "updated_at"))

    def test_amount_attr(self):
        """Test that Expense has attr amount, and it's of type float"""
        expense = Expense()
        self.assertTrue(hasattr(expense, "amount"))
        self.assertIsInstance(expense.amount, float)

    def test_description_attr(self):
        """Test that Expense has attr description, and it's of type string"""
        expense = Expense()
        self.assertTrue(hasattr(expense, "description"))
        self.assertIsInstance(expense.description, str)

    def test_category_attr(self):
        """Test that Expense has attr category, and it's of type string"""
        expense = Expense()
        self.assertTrue(hasattr(expense, "category"))
        self.assertIsInstance(expense.category, str)

    def test_user_id_attr(self):
        """Test that Expense has attr user_id, and it's of type integer"""
        expense = Expense()
        self.assertTrue(hasattr(expense, "user_id"))
        self.assertIsInstance(expense.user_id, int)
        self.assertTrue(hasattr(expense, "__tablename__"))
        self.assertEqual(expense.__tablename__, 'expenses')
