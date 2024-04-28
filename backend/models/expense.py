#!/usr/bin/python3.
"""Contains an Expense class"""

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class Expense(BaseModel, Base):
    """Representation of an expense."""
    __tablename__ = 'expenses'
    amount = Column(Float, nullable=False)
    description = Column(String(255))
    category_id = Column(String(60), ForeignKey('categories.id'))
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category = relationship("Category", back_populates="expenses")
    user = relationship("User", back_populates='expenses')

    @property
    def categories(self):
        """Getter attribute returns the list of Category instances"""
        from models.category import Category
        category_list = []
        all_categories = models.storage.all(Category)
        for category in all_categories.values():
            if category.user_id == self.id:
                category_list.append(category)
        return category_list

    @property
    def users(self):
        """Getter attribute returns the list of User instances"""
        from models.user import User
        user_list = []
        all_users = models.storage.all(User)
        for user in all_users.values():
            if user.id == self.id:
                user_list.append(user)
        return user_list
