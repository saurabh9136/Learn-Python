"""
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.
”python”,“java”,“C++”,“python”,“javascript”,
“java”,“python”,“java”,“C++”,“C”
"""
subject = {"python","java","C++","python","javascript", "java", "python", "java","C++", "C" }

uniqueSubjects = set(subject)
print("total number of classrooms are", len(uniqueSubjects))

"""Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)"""

set = {
    ("float", 9.0),
    ("int", 9)
}
print(set)