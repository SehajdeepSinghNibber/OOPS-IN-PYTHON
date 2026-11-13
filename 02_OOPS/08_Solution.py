# Static Method
# Add a static method to the Car class that returns a general description of a car

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

    @staticmethod
    def general_desc():
        return "Cars are a means of transport"

class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


print(Car.total_car)

my_car = Car("Tata","Safari")

# print(my_car.general_desc())
print(Car.general_desc())