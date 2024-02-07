import random

target_number = random.randint(1, 10)

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess > target_number:
        print("Too high!")
    elif user_guess < target_number:
        print("Too low!")
    else:
        print("Correct!")
        break