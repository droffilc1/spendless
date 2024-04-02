#!/usr/bin/python3
"""The BaseModel class module."""
from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializing the instances

        Args:
        id: string - assigned with an uuid when an instance is created.
        created_at: datetime - assigned with the current datetime when
                    an instance is created.
        updated_at: datetime - assign with the current datetime when an
                    instance is created and it will be updated every time
                    you change your object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strftime(kwargs['created_at'], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strftime(kwargs['updated_at'])
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __repr__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updates the public instance attribute updated_at
        with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        result_dict = self.__dict__.copy()
        result_dict.pop('_sa_instance_state', None)
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict

    def delete(self):
        """Delete the current instance from the storage
        """
        models.storage.delete(self)
