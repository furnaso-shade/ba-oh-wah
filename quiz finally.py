questions = ("who's the best programmer in the world?", "who's the best mango eater in the world?", "who's the tallest person in the world")

options = (("florin", "cobram", "rambo", "sithima"),
           ("tlipo", "hokila", "weinita", "rambo"),
           ("xmifoq", "rambo", "plokili", "dgidga"))
guesses = []
answers = ("rambo", "rambo", "rambo")
score = 0

for x in range(0, 3):
    useroption = input(f"""{questions[x]} 
options = {options[x]}. enter your guess: """)
    if useroption == answers[x]:
        print("CORRECT!!! 😍")
        score += 1
    else:
        print("wrong man, guess again 😢")

print(f"your score is {score}")

print("lets go you got em alll" if score == 3 else "you suck b###h"  )





