# Ploymorphism operator oerloading

# When the same operator is allowed to have the difference meaning according to context

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, " i", self.img, "j")
    
    # def add(self, num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)
    
    #creating a dunder funcion for add just need to add __ before and afte the function name
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
c1 = Complex(3, 2)
c2 = Complex(1, 5)

c3 = c1 + c2
c3.showNum()
c4 = c1 - c2
c4.showNum()




