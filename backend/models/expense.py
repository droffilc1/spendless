#!/usr/bin/python3.
"""Contains an Expense class"""

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Expense(BaseModel, Base):
    """Representaiton of an expense."""
    __tablename__ = 'expenses'
    amount = Column(Float, nullable=False)
    description = Column(String(255))
    category_id = Column(String(60), ForeignKey('categories.id'))
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category = relationship("Category", back_populates="expenses")
    user = relationship("User", back_populates='expenses')
