from .showroom import Showroom

class Dealership:
    def __init__(self, name: str, capacity: int):#, showrooms: List[Showroom] = []):
        self.__name = name
        self.__capacity = max(0, capacity)
        self.__showrooms = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def showrooms(self):
        return self.showrooms

    def add_showroom(self, showroom: Showroom):
        if len(self.__showrooms) == self.capacity:
            raise ValueError('ERROR: The dealership is already at capacity.')
        else:
            self.__showrooms.append(showroom)