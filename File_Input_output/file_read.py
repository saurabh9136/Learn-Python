"""
Reading a file

data = f.readline( ) #reads one line at a time
data = f.read( ) #reads entire file
"""

f = open("D:\\Personal\\learn Python\\File_Input_output\\demo.txt", "r") #read only

readFirstletter = f.read(5) #number of letter
readLine = f.readline() #read one line at a time
readHoletext = f.read() # read all data

print(readLine)
f.close()

file1 = open("D:\\Personal\\learn Python\\File_Input_output\\demo.txt", "r+") #read and write no truncate
file1.write("extra text")

print(file1)

# with Syntax
with open("D:\\Personal\\learn Python\\File_Input_output\\demo.txt", "r") as f: #as stands for alias
    data = f.read()

print(data)
# no need to close the file as with syntax handle it

