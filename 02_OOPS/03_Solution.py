# Inheritance
# Create an ElectricCar class that inherits from the Car class and has additional attribute battery_size

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Brand:{self.brand}\nModel:{self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85 kWh")

print(my_tesla.model)
print(my_tesla.fullName())
print(my_tesla.battery_size)