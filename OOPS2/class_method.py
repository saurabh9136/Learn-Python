"""
class method
A class method is bound to the class & receives the class as an implicit first argument.
Note - static method can't access or modify class state & generally for utility.
"""
class Person :
    name = "saurabh"

    # def __init__(self, name):
    #     self.__class__.name = name #self = boject, class = person, 

    # same work using class methods 
    @classmethod
    def changeName(cls, name):
        cls.name = name


p = Person("shubham")

print(p.name)
print(Person.name)

