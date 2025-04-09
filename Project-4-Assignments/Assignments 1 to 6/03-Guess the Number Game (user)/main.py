import random

print(" Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 10)
print("I have secret number between 1 to 10, can you guess the number?")

while True:
    try:
        guess = int(input("entr your guess: "))
        if guess > secret_number:
            print("Too high! try again")
        elif guess < secret_number:
            print("Too low! try again.")
        else:
            print("Congratulation! You have guessed the number!")
            break
    except ValueError:
         print("Invalid input, Please enter a number between 1 - 10")

