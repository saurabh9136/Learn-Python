#WAP to calculate the product of two number

def cal_prod(a, b):
    return a*b

print(cal_prod(39, 2))

"""
Default Parameters

Assigning a default value to parameter, which is used when no argument is passed.
"""

def cal_prod_default(a, b=5):
    return a*b

print(cal_prod_default(3))