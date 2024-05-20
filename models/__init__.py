#!/usr/bin/python3
"""
this is what will instantiate the object of my class FileStorage and it then reloads it.
"""

from models.engine.file_storage import FileStorage

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
