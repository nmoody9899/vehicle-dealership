from vehicle import Vehicle

class Showroom:
    def __init__(self, name: str, capacity: int):
        self.__name = name
        self.__capacity = max(0, capacity)
        self.__vehicles = []

    @property
    def name(self):
        return self.__name

    @property
    def name(self):
        return self.__capacity

    @property
    def vehicles(self):
        return self.__vehicles

    def add_vehicle(self, vehicle: Vehicle):
        if len(self.__vehicles) == self.capacity:
            raise ValueError('ERROR: The showroom is already at capacity.')
        else:
            self.__vehicles.append(vehicle)