# Guess the numebr

import random

rand_num = random.randint(0, 200)
print("If u wanna surrender just type 1000")
inp_num = int(input("Enter your guess: "))
while True:

    if (inp_num > rand_num and inp_num != 1000):
        print("Try a smaller number please")
        inp_num = int(input())

    elif inp_num < rand_num:
        print("Try a greater number pls: ")
        inp_num = int(input())
    elif inp_num == rand_num:
        print("Congrats u guessed the number!!")
        break
    elif inp_num == 1000:
        print("U chose to surrender but the nmber u tried to guess is", rand_num)
        break
