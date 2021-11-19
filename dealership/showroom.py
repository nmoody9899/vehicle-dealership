from vehicle import Vehicle

class Showroom:
    def __init__(self, name: str, capacity: int, vehicles: List[Vehicle] = []):
        self.__name = name
        self.__capacity = capacity

    @property
    def name(self):
        return self.__name

    @property
    def name(self):
        return self.__capacity