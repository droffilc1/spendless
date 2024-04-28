#!/usr/bin/python3
"""Contains categories class."""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class Category(BaseModel, Base):
    """Representation of a category."""
    __tablename__ = 'categories'
    name = Column(String(50), unique=True, nullable=False)
    expenses = relationship('Expense', back_populates='category',
                            cascade='all, delete-orphan')

    @property
    def expense(self):
        """Getter attribute returns the list of Expense instances"""
        from models.expense import Expense
        expense_list = []
        all_expenses = models.storage.all(Expense)
        for expense in all_expenses.values():
            if expense.user_id == self.id:
                expense_list.append(expense)
        return expense_list
