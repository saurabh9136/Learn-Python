# Super method

# super() is used to access methods of the parent class

class Car:

    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start() :
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")    

class Toyota(Car) :

    def __init__(self, name, type):
        self.name = name
        #here I need to call type from car class
        super().__init__(type) #syntax to call super method
        super().start()


c1 = Toyota("harrier", "electric")
print(c1.type)
