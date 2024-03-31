"""_ _init_ _ Function

All classes have a function called __init__(), which is always executed when the object is being initiated.

Constructor

*The self parameter is a reference to the current
instance of the class, and is used to access variables
that belongs to the class."""

class Student:
    # the data/varaibls store in class is known as attribute
    college_name = "CSC college" #if same value need to store for all user then init here instead in constructor
    # parameterized constructor
    def __init__(self, fullname, marks): #self is always first parameter
        # print(self) #<__main__.Student object at 0x000002256A609B80>
        self.name = fullname #onject attribute
        self.marks = marks
    
    # default constructor
    def __init__(self):
        pass



s1 = Student("shubham", 89)
print(s1.name)


s2 = Student("Saurabh", 91)
print(s2.name, end=" ")
print(s2.marks)