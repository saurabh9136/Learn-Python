
# single line ternay operator with statement 

food = input("food Name: ")
print("sweet") if(food=="jalebi" or food == "gulabjamun") else print("Not sweet") 

# ternary operator with var
age = int(input("your age: "))
result = "eligible" if(age >= 18) else "not eligible"
print(result)

#Clever If/Ternary Operator
# syntax = <var> = (false_val, \true_val [<condition>]
vote = ("yes", "no") [age < 18]
print(vote)

#calculate tax

salary = float(input("your salary"))
tax = salary*(0.1, 0.2) [salary >= 50000]
print(tax)