# WAF to print the length of a list. ( list is the parameter)
list = [2, 4, 3, 1, 6 ,7, 5, 4]

def print_len(list):
    return len(list)

# WAF to print the elements of a list in a single line. ( list is the parameter)
def print_elemnts(list):
    for val in list:
        print(val, end=" ")


# WAF to find the factorial of n. (n is the parameter)
def cal_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i    
    
    return fact


# WAF to convert USD to INR.

def usd_to_inr(value):
    return  float(value*83.33) #current value

print("length of list is", print_len(list))
print("elemnts in single line", print_elemnts(list))
print("factorial of number is: ", cal_factorial(5))
print("INR:", usd_to_inr(5))

# WAF to checkthe input number is odd or evem

def odd_or_even(n):
    return "even" if n%2 == 0 else "odd"

print(odd_or_even(6))