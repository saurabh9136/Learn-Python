collection = set()

#adds an element
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(1) # not add into list

collection.add((1, 2, 4))

#remove an element
collection.remove(2)

#clear the set
collection.clear()

#to pop any data
# collection.pop()


# print(collection)

"""
Set is the collection of the unordered items.
Each element in the set must be unique & immutable.
"""
#combines both set values & returns new
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

#combines common values & returns new
print(set1.intersection(set2))