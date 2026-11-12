# Basic Class And Object
# Create a class Car with attributes like brand and model.Then Create an Instance of class

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota","Camry")

print(my_car)
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car)
print(my_new_car.brand)
print(my_new_car.model)

# __init__ is constructor