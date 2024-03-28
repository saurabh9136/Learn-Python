# Print the elements of the following list using a loop:

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for el in list:
#     print(el)

# Search for a number x in this tuple using loop:
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x = int(input("Enter a number you want to find in Tuple: "))
# for val in tup:
#     if(val == x):
#         print("founded at index of:", tup.index(val))
#         break
# else:
#     print("not found")

#WAP to find the factorial of first n numbers. (using for)
x = int(input("Enter a number you want to find the factorial value: "))
fcat = 1
for i in range(1,x+1):
    fcat *= i

print(fcat)
