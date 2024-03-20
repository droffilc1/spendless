#!/usr/bin/python3.
"""Contains an Expense class"""

from sqlalchemy import Column, String, Float, Integer, ForeignKey
from models.base_models import BaseModel, Base


class Expenses(BaseModel, Base):
    """Representaiton of an expense."""
    __tablename__ = 'expenses'
    amount = Column(Float, nullable=False)
    desciption = Column(String(255))
    category = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
