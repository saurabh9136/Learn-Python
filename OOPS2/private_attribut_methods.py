"""Private(like) attributes & methods
conceptual implementation in python 
private attributes & methods are mean to be used only within the class and are not accessible outside the 
class"""

#sybtax used __ before attribute

class AC:
    def __init__(self, ac_no, passw):
        self.__ac_no = ac_no
        self.__passw = passw 
    
    def reset_pass(self):
        return self.__passw
    
a1 = AC("1234", "sdfg")
# print(a1.ac_no)
print(a1.reset_pass())

#  for methods

class Person :
    __name = "Saurabh"
    def __private_method(self):
        print("Inside private method")
    
    def access_private_method(self):
        self.__private_method()
    
p = Person()
print(p.access_private_method())
