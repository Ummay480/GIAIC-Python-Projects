import random
print("Welcome to the Number Guessing Game!")


low = 1
high = 10

print("Think of a number between 1 to 10 and computer will be guess the number")

if low <= high:
    guess = random.randint(low, high)
    print("Computer's guess is: ", guess)

while True:
    feedback = input("Is the guess too high (H), too low (L), or correct(C)")
    if feedback == "C":
        print("yeh! The Computer guessed your number")
        break
    elif feedback == "H":
        high = guess - 1
        guess = random.randint(low,high)
        print("Computer's guess is: ", guess)
    elif feedback == "L":
        low = guess + 1
        guess = random.randint(low, high)
        print("Computer's guess is: ", guess)
    else:
        print("Invalid input. Please enter H,L,C.")

if low > high:
    print("the number is not in range, Please try again.")
    
