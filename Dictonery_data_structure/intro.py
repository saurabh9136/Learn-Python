"""
Dictionary in Python
Dictionaries are used to store data values in key:value pairs
They are unordered, mutable(changeable) & don't allow duplicate keys
"""
# Dictionary denote by {}

nullDict = {} #empty/null dict
print(type(nullDict))

info = {
    "key" : "Value",
    "Name" : "Saurabh",
    "Age" : 22,
    "is_adult" : True,
    "subject" : [ "Java", "python"],
    "topic" : ("List", "Tuple", "dictonery")
}

print(info["Name"]) #acces data using key
info["Name"] = "Saurabh Giri" # as its mutable
info["surname"] = "giri" #using this we can add new parameter
print(info)