#!/usr/bin/python3
"""
This module contains the Rectangle classs
"""

from models.base import Base


class Rectangle(Base):
    """My rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle class"""
       self.width = width
       self.height = height
       self.x = x
       self.y = y
       super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @width.setter
    def width(self, val):
        """setter of width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """setter of height"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """setter of x"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @y.setter
    def y(self, val):
        """setter of y"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """returns area value of Rectangle"""
        return self.__width * self.__height

    # write other funcs 

    def update(self, *args, **kwargs):
        """this updates the attributes"""
        if len(args):
            for i, a enumerate(args):
                if i = 0:
                    self.id = a
                elif i = 1:
                    self.width = a
                elif i = 2:
                    self.height = a
                elif i = 3:
                    self.x = a
                elif i = 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "width" in kwargs:
                self.width = kwargs["width"]
            elif "height" in kwargs:
                self.height = kwargs["height"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.y = kwargs["y"]











