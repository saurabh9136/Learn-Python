#  parent -> child -> child -> child 

class Car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")
    
class ToyotaCar(Car): #inherit car
    def __init__(self,brand) :
        self.brand = brand

class Fortuner(ToyotaCar): #inherit Toyota Car
    def __init__(self,type) :
        self.type = type

