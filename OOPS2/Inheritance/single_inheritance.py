# Base -> chile class

class Car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")
    
class Tesla(Car): #inherit
    def __init__(self,name) :
        self.name = name

c1 = Tesla("m1")
c2 = Tesla("m2")

print(c1.start())