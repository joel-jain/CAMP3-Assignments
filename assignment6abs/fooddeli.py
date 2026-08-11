from abc import ABC, abstractmethod
class FoodOrder(ABC):
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    @abstractmethod
    def place_order(self):
        pass
    @abstractmethod
    def calculate_bill(self):
        pass
class VegOrder(FoodOrder):
    def calculate_bill(self):
        return self.quantity * self.price
    def place_order(self):
        print("Veg order placed")
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.calculate_bill())
class NonVegOrder(FoodOrder):
    def calculate_bill(self):
        return self.quantity * self.price
    def place_order(self):
        print("Non-Veg order placed")
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.calculate_bill())
veg = VegOrder(2, 120)
nonveg = NonVegOrder(3, 180)
veg.place_order()
print()
nonveg.place_order()
