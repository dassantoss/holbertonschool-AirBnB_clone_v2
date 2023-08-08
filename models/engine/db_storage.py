#!/usr/bin/python3
"""
    This module defines a class to manage storage of hbnb models using
    SQL Alchemy
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from models.base_model import Base


class DBStorage:
    """ manage storage of hbnb models using SQL Alchemy """
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine (self.__engine)"""

        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """
            Query on the current database session all objects depending
            of the class name
        """
        dict_cls = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dict_cls[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            list_class = [State, Place, User, City, Review, Amenity]
            for every_class in list_class:
                for ob in self.__session.query(every_class).all():
                    dict_cls[ob.to_dict()['__class__'] + '.' + ob.id] = ob
        return dict_cls

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        and create the current database session by by using a sessionmaker """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        self.__session = Session()

    def close(self):
        self.__session.close()
