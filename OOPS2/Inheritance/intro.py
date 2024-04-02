# Inheritance

# When one class(Child/derived) derives the properties & methods of another(parent/base)

class Car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")
    
class Tesla(Car):
    def __init__(self,name) :
        self.name = name

c1 = Tesla("m1")
c2 = Tesla("m2")

print(c1.start())