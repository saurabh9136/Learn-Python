#  condition statement

light = input("what is a light color: ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("slow down")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#WAP to check if a number entered by the user is odd or even.
userInput = int(input("enter a number"))
print("even") if((userInput % 2) != 0) else print("odd")

#WAP to find the greatest of 3 numbers entered by the user.
input1 = int(input("enter a first value: "))
input2 = int(input("enter a second value: "))
input3 = int(input("enter a third value: "))

if(input1 > input2 and input1 > input3):
    print("input1 is greatest", input1)
elif(input2 > input3):
    print("input 2 is greatest", input2)
else:
    print("input3 is greatest")


#WAP to check if a number is a multiple of 7 or not
userInput = int(input("enter a number"))
if(userInput % 7 == 0):
    print(userInput, " is a multiple of 7")
else:
    print(userInput, "is not a multiple of 7")