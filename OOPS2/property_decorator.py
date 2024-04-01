# Property decorator

# We use @property decorator or any method in the class to use the method as a property

class Student:
    def _init_(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
stu1 = Student(98, 97, 99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)