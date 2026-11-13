# Polymorphism
# Demonstrate a Polymorphism by defining method fuel_type in both Car and ElecrticCar classeses, but woth different behaviour

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand+"!"

    def fullName(self):
        return f"Brand:{self.__brand}\nModel:{self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
            return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85 kWh")

print(my_tesla.model)
print(my_tesla.fuel_type())