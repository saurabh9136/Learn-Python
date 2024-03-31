"""
Hiding the implementation details of a class and only showing the essential features to the user.
"""

class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
    
    def start(self):
        self.acc = True #this code explain the abstraction
        self.brk = True
        print("car is started")
    
c1 = Car()
c1.start()