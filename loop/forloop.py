# Loops are used used for sequential traversal. For traversing list, string, tuples etc.?
    
# syntax - for var/item/val in list/tuple/dict/set :
# in is a keyword

list = [1, 2, 3, 5] 
veggies = ["potato", "onion", "tomato", "ladyfinger"]

for el in veggies:
    print(el)


tup = (1, 2, 3, 4, 5, 6, 7)
for val in tup:
    print(val)

# for Loop with else
# syntax - 
for el in list:
    print(el)
else:
    print("all elements are printed")