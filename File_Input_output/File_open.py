# code to open the file

f = open("D:\\Personal\\learn Python\\File_Input_output\\demo.txt", "r")

data = f.read()
print(type(data))
f.close()

"""
Character                       Meaning

'r'                     open for reading (default)
'w'                     open for writing, truncating the file first
'x'                     create a new file and open it for writing
'a'                     open for writing, appending to the end of the file if it exists
'b'                     binary mode
't'                     text mode (default)
'+'                     open a disk file for updating (reading and writing)

"""