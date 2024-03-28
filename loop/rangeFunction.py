# Range functions returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and stops before a specified number.

# range( start?, stop, step?) #? meaning optional

for i in range(10): #single value means (stop) value
    print(i) 

for i in range(1, 10): #double value means (start stop)
    print(i) 

for i in range(1, 10, 2): #3 value means (start, stop, step size) value
    print(i) 


# Print numbers from 1 to 100.
for i in range(1, 11):
    print(i)

# Print numbers from 100 to 1.
for i in range(11, 0, -1):
    print(i)

# Print the multiplication table of a number n.
n = int(input("enter a number: "))
for i in range(1, 11):
    print(n," X ", i, "=", i*n)

# pass is a null statement that does nothing. It is used as a placeholder for future code.
for i in range(4):
    pass



