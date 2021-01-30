# Guess the numebr

# We have to make a number guessing game in which i have to tell number off guesses it too and number of guesses remaining and i not guessed in 9 time print game over
def popu():
    import random
    guessing_number = random.randint(0, 100)
    i = 0
    print("-------------Hello You have to guess the number in 9 times if not guessed in 9 turns then game over!------------")
    while True:
        guessed_number = int(input("Enter your guess: \n"))
        i += 1
        if i != 9:
            if guessed_number == guessing_number:
                print("Congratulations You guessed the number in ", i, " turns")
                break
            elif guessing_number > guessed_number:
                print("Try a bigger number!")
                print(9-i, "Turns left")
                continue
            elif guessed_number > guessing_number:
                print("Try a smaller number!")
                print(9-i, "Turn left")
                continue
        else:
            print("Game over!, The number was", guessing_number)
            break


if __name__ == '__main__':
    popu()
