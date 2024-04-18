#!/usr/bin/python3
"""
This is the `rectangle` class
"""

class Rectangle(Base):
    """the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    ## define the getters for x and y

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=0")
        self.__x = value

    ## define the setters for height and y

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if len(args):
            for i, arg enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "width" in kwargs:
                self.width = kwargs["width"]
            elif "height" in kwargs:
                self.height = kwargs["height"]
            # Complete for x and y




