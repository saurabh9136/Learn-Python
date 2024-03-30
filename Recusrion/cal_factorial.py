# calculate the factorial of n 

def cal_fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * cal_fact(n - 1)

print(cal_fact(5))