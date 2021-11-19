class Vehicle:
    def __init__(self, year: int, make: str, model: str, price: float, mileage: int=0):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__price = float(format(max(0, price), '.2f'))
        self.__mileage = max(0, mileage)

    @property
    def year(self):
        return self.__year

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def price(self):
        return self.__price

    @property
    def mileage(self):
        return self.__mileage 

    @property
    def year_make_mode(self):
        return f'{self.__year} {self.__make} {self.__model}'