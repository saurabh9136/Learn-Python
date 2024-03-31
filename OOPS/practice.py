"""
Let‘s Practice
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
"""
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def Know_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum/3

s1 = Student("Saurabh", [83, 93, 35])
print("Hi",s1.name, "your avg score is: ", s1.Know_avg())
