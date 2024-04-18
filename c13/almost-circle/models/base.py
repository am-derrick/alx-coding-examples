#!/usr/bin/python3
"""
This module contains the Base class
"""


class Base:
    """My Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises the Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
