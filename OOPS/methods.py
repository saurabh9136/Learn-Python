"""
Methods
Methods are functions that belong to objects.

class is a collection of attributes and methods
"""

class Car:
    compan = "Tesla"
    def __init__(self, model, price):
        self.model = model
        self.price = price
    
    def speed(slef):
        print("speed is more then rocket")

    def getPrice(self):
        return self.price

c1 = Car("X1", 70000)
print(c1.getPrice())
# print(c1.compan, c1.model, c1.price)
# c1.speed()
