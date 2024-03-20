#!/usr/bin/python3
"""Contains User class"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_models import BaseModel, Base


class User(BaseModel, Base):
    """Representation of a user."""
    __tablename__ = 'users'
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    expenses = relationship('Expense', backref='user', lazy=True)
