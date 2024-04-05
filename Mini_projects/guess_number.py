import random

random_number = random.randint(1, 100)   

while True:
    user_number = input("guess the target or Qiut(q): ")
    if(user_number == "q"):
        break

    if(user_number == random_number) :
        print("wohoo, you guessed the current number")
        print("----------GAME OVER ---------")
        break
    elif(user_number > random_number) :
        print("you entered a greater number try with smaller value")
    else:
        print("you entered a smaller number try with greater value")

