#!/usr/bin/python3
"""Contains the class DBStorage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.base_model import BaseModel, Base
from models.category import Category
from models.user import User
from models.expense import Expense


classes = {"User": User, "Category": Category, "Expense": Expense}


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Intantiates a DBStorage object"""
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST')
        MYSQL_DB = getenv('MYSQL_DB')
        ENV = getenv('ENV')
        self.__engine = create_engine('mysql://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current databasse session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Add the object to the current dtatabase session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Call remove methid on the private instance attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
