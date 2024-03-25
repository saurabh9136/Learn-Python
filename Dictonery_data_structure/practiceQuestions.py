"""
WAP to Store following word meanings in a python dictionary :
table : “a piece of furniture”,“list of facts & figures”
cat : “a small animal”
"""

py_dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

# print(py_dict)

"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value."
"""

student_dict = {}
user_input1 = input("Enter your Phy Marks one by one")
student_dict.update({"Phy": user_input1})
user_input = input("Enter your Chem Marks one by one")
student_dict.update({"Chem": user_input})
user_input2 = input("Enter your CS Marks one by one")
student_dict.update({"CS": user_input2})

print(student_dict)