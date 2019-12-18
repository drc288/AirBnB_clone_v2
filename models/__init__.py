#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

if getenv('HBNB_TYPE_STORAGE') == 'db':
    # from models.engine.db_storage import DBStorage
    # create an instance of DBSstorage store it in storage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
