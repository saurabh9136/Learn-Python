# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
userInput = []
input1 = input("enter first favorite movie Name ")
input2 = input("enter second favorite movie Name ")
input3 = input("enter thirs favorite movie Name ")

userInput.append(input1)
userInput.append(input2)
userInput.append(input3)
print("Movies are", userInput)

userInput = [input("enter first favorite movie Name: "), input("enter second favorite movie Name: "), input("enter thirs favorite movie Name: ")]


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# [1, 2, 3, 2, 1] [1, "abc", "abc", 1]

list = ["m", "a", "a", "m"]
copy_list = list.copy() # return shallow copy  
copy_list.reverse()

print(list == copy_list)