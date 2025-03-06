logo = """   ________                                     __   .__                                       ___.                   
 /  _____/  __ __   ____    ______  ______   _/  |_ |  |__    ____       ____   __ __   _____ \_ |__    ____ _______ 
/   \  ___ |  |  \_/ __ \  /  ___/ /  ___/   \   __\|  |  \ _/ __ \     /    \ |  |  \ /     \ | __ \ _/ __ \\_  __ \
\    \_\  \|  |  /\  ___/  \___ \  \___ \     |  |  |   Y  \\  ___/    |   |  \|  |  /|  Y Y  \| \_\ \\  ___/ |  | \/
 \______  /|____/  \___  >/____  >/____  >    |__|  |___|  / \___  >   |___|  /|____/ |__|_|  /|___  / \___  >|__|   
        \/             \/      \/      \/                \/      \/         \/              \/     \/      \/         """

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

import random
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("Too high.")
        attempts -= 1
    else:
        print("Too low.")
        attempts -= 1 

if attempts == 0:
    print("You've run out of guesses, you lose.")



