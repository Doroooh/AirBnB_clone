#!/usr/bin/python3

"""__init__ magic method to initialize package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
