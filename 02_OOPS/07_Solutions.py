class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fullName(self):
        return f"Brand:{self.__brand}\nModel:{self.model}"


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


print(Car.total_car)