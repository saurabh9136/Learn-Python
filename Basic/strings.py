# string with space
stringSpace = "Hi this is a saurabh giri \t first day learning python"

#string in next line
stringNextLine = "Hi this is a saurabh giri \n first day learning python"

#concate 2 string
str1 = "hi this a saurabh giri"
str2 = "first day learning python"
concatStr = str1 + str2

#count length of string
strLen = len(str1) # spaces are also countable

#access char using index in string
index = str1[5]

"""
we cannot manipulate string through index
str1[5] = 'j'
not allowed 
"""

# slicing - accessing part of string same as substring
#syntax = str[starting_idx : ending_idx] ending_idx is not included

slice = str1[0:8] # or [:8]
slice2 = str1[8: len(str1)] # or [8:]

#negative
negativeSlice = str1[-10 : -1]

# string functions
endwithFuc = str1.endswith("ri") #returns true if string ends with substr
capitalString = str1.capitalize() #capitalizes 1st char
replaceWords = str1.replace( "saurabh", "Avinash") #replaces all occurrences of old with new
findWord = str1.find("saurabh") #returns 1st index of 1st occurrence
countofString = str1.count("a") #counts the occurrence of substr in string

# print(countofString)


#WAP to input user's first name & print its length.
userName = input("Enter your name ")
print("length is: ", len(userName))
#WAP to find the occurrence of '$' in a String.
string = "jhbd$&H%##&$@%$$^$#$"
print("the count of $ in string is: ", string.count("$"))