#!/usr/bin/python3
"""Contains User class"""

from flask_login import UserMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base, UserMixin):
    """Representation of a user."""
    __tablename__ = 'users'
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    expenses = relationship('Expense', back_populates='user',
                            cascade='all, delete-orphan')
