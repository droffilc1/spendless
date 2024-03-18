#!/usr/bin/python3
"""Contains categories class."""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_models import BaseModel


class Categories(BaseModel):
    """Representation of a category."""
    name = Column(String(50), unique=True, nullable=False)
    expenses = relationship('Expense', backref='category', lazy=True)
