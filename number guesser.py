import random

guess = random.randint(1, 100)
turns = 0

while True:
    answer = int(input("guess a number from 1 to 100: "))
    turns += 1
    if guess > answer:
        print("you are low balling dude!")
    elif guess < answer:
        print("you are high balling dude!")
    else:
        print(f'''--------------------------
you guessed correct! It took you {turns} turns though 😒''')
        break

