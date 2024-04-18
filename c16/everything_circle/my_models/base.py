class Base:
    """document your class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """document that"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
