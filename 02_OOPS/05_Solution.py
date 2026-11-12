
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    # Getter
    def get_brand(self):
        return self.__brand + "!"

    # Setter
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def fullName(self):
        return f"Brand: {self.__brand}\nModel: {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")

# Access using getter
print(my_tesla.get_brand())

# Modify using setter
my_tesla.set_brand("Porsche")

# Access updated value
print(my_tesla.get_brand())

print(my_tesla.fullName())
