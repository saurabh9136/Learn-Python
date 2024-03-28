# Print numbers from 1 to 100.
count = 1
while count <=100:
    # print(count)
    count += 1
    
# Print numbers from 100 to 1.
count = 100
while count >=1:
    # print(count)
    count -= 1

#Print the multiplication table of a number n.
# user_input = int(input("enter a number: "))
count = 1
while count <=10:
    # print(count * user_input)
    count +=1

# Print the elements of the following list using a loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx = 0
while idx < len(list):
    # print(list[idx]) 
    idx+=1

# Search for a number x in this tuple using loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
    
number = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
user_input2 = int(input("enter a number: "))
i = 0
answer : False
while i < len(list):
    if(number[i] == user_input2):
        print("at index", i)   
        break
        i +=1
    else:
        print("founding")
        i+=1

# WAP to find the sum of first n numbers. (using while)
n = int(input("enter a number: "))

i = 0 #index
sum = 0 #calculate sum
while i<=n:
    sum += i
    i+=1

print("sum of n numbers are:", sum)

