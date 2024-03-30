# Write a recursive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if n == 1 :
        return 1
    else:
        return n + cal_sum(n-1)
    
print(cal_sum(5))

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_list(lst, index):
    if index >= len(lst):
        return
    else:
        print(lst[index])
        print_list(lst, index + 1)


print_list([1, 2, 3, 4, 5, 6], 7)