# Class Method and Self
# Add a method to a Car class that displays the full name of the car (brand and model)

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Brand:{self.brand}\nModel:{self.model}"

my_car = Car("Toyota","Camry")

print(my_car.fullName())