#!/usr/bin/python3
"""Selects a storage method based on the environment"""
from models.engine.file_storage import FileStorage
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
