"""
Static Methods
Methods that don’t use the self parameter (work at class level)

#decorator
*Decorators allow us to wrap another function in order to
extend the behaviour of the wrapped function, without
permanently modifying it
"""

class Student:

    @staticmethod
    def hello():
        print("Hi, welcome")

s1 = Student()
s1.hello()