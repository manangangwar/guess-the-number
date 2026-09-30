import random
import time
import math


def welcome():
    print("================================")
    print("       GAMBLE AT YOUR OWN RISK  ")
    print("================================")
    print("You have 3 chances to guess the number.")
    print()


def guessing_game():

    fixed_number = random.randint(1, 10)

    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:

        guess = int(input('Your guess is: '))
        guess_count += 1

        if guess == fixed_number:
            print("""YOU WON!!! HEE - YAAA

             ♫      *\O*/     ♫
                    |
                   / *\\*   <3""")

            print("You guessed the number correctly!")
            print("Game finished in", math.ceil(time.time() % 60), "seconds.")
            break

        else:
            print('YOUR GUESS WAS WRONG')
            print('YOU HAVE {} GUESSES LEFT'.format(guess_limit - guess_count))

            if guess_count < guess_limit:
                time.sleep(1)

    if guess != fixed_number:
        print("""YOU LOST!!!
              (╥﹏╥)""")
        print("The correct number was:", fixed_number)


def main():
    welcome()
    guessing_game()


main()