"""del keyword

Used to delete object properties or object itslef"""


class Student:
    def __init__(self, name) :
        self.name = name

s1 = Student("Saurabh")

print(s1)
del s1 