#!/usr/bin/python3
"""
This module has the `Base' class
"""


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
