#!/usr/bin/python3
"""__init__ magic is the technique to initialize for models directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
