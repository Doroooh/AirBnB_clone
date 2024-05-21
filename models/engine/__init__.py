#!/usr/bin/python3
"""Initializing the package for the project"""
"""init file in models/engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
