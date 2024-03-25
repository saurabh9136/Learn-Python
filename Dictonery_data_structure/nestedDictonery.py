# Nested Dictonry

# scenerio is lets suppose need to store the student subject with marks here we need to use nested dict

student = {
    "name" : "Saurabh",
    "subject" : {
        "sci" : 89,
        "Maths" : 93,
        "Chem" : 75
    }
}

print(student["subject"]["Chem"])