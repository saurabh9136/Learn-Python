"""
Define a Circle class to create a circle with radius r using the constructor.
Define an Area) method of the class which calculates the area of the circle.
Define a Perimeter) method of the class which allows you to calculate the perimeter of the circle.
"""

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return (22/7) * self.r**2
    
    def perimiter(self):
        return 2 * (22/7) * self.r

c = Circle(21)

print(c.area())
print(c.perimiter())

"""
Define a Employee class with attributes role, department & salary. This class also a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additionalattributes:

name & age

"""

class Employee:

    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    
    def showDetails(self):
        print("role", self.role)
        print("Department", self.dept)
        print("Salary", self.sal)

e1 = Employee("SDE", "It", 45000)
e1.showDetails()

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 75000)

eng = Engineer("elon musk", 40)
eng.showDetails()
    
"""
Qs. Create a class called Order which stores item & its price.

Use Dunder function_gt_() to convey that:

order1 > order2 if price of order1 > price of order2
"""
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price
    
ord1 = Order("chips", 50)
ord2 = Order("chocolate", 100)

print(ord2 > ord1)