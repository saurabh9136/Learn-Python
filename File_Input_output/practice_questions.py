"""
Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Python.
I like A programing in python.
"""

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone \n I am learning File I/O \n using Java. \nI like A programing in Java")


# WAp that replace all occurrences of “java” with “python” in above file.

# with open("practice.txt", "r") as f:
#     data = f.read() #data is a string value

# new_data = data.replace("Java", "python")
# print(new_data)

# with open("practice.txt", "w") as w:
#     w.write(new_data)

# Search if the word “learning” exists in the file or not.
# search_word = "learning"

# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(search_word) != -1):
#         print("Founded")
#     else:
#         print("Not found")


# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.
def find_line():
    line_count =1 #initialy start from first line
    word = "saurabh" 
    data = True
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_count)
                return
            line_count +=1
    return -1        

# find_line()


# From a file containing numbers separated by comma, print the count of even numbers.
def count_even():
    with open("practice.txt", "r") as f:
        data = f.read()
        # num = ""
        # for i in range(len(data)):
        #     if(data[i] == ","):
        #         print(int(num))
        #         num = ""
        #     else:
        #         num += data[i]

        num = data.split(",")
        count = 0
        for i in num:
            if(int(i) % 2 == 0):
                count += 1
       
    return count
print(count_even())