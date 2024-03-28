#!/usr/bin/python3
"""Contains categories class."""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Category(BaseModel, Base):
    """Representation of a category."""
    __tablename__ = 'categories'
    name = Column(String(50), unique=True, nullable=False)
    expenses = relationship('Expense', back_populates='category', lazy=True)
