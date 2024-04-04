import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

charValues = string.ascii_letters + string.digits + string.punctuation
pass_len = 12

pasword = ""

for i in range(pass_len):
    pasword += random.choice(charValues)

print(pasword)

# list comprehension syntax
res = [random.choice(charValues) for i in range(pass_len)]
print(res)
