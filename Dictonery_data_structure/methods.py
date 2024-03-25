student = {
    "name" : "Saurabh",
    "subject" : {
        "sci" : 89,
        "Maths" : 93,
        "Chem" : 75
    }
}

student.keys() # return all keys

student.values() #return all values

student.items() # return all (key, val) pairs as tuple

#return the key according to value
print(student.get("name")) #if key is not there it will retuen none

student.update({"city": "Mumbai"}) #insert the specified items to the dict

print(student)

# print(len(student.keys()))
# print(list(student.keys())) #storing keys in list format instead dictkeys