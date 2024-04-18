class Rectangle(Base):
    """document my rectangle class"""
    def __init__(self,  width, height, x=0, y=0, id=None):
        """have this documentated"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    # go and write getters for height, x and y

    @width.setter
    def width(self, val):
        """documentation"""
        if type(val) is not int:
            raise TypeError("width should be an integer")
        if val <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = val

    # write setters for height, x and y

    def update(self, *args, **kwargs):
        """add documentation"""
        if len(args):
            for i, a enumerate(args):
                if i = 0:
                    self.id = a
                elif i = 1:
                    self.width = a
                elif i = 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "width" in kwargs:
                self.width = kwargs["width"]

            #####
            dict = {}
           dict["id"] = self.id
           return dict
