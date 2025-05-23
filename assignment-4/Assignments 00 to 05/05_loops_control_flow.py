# -*- coding: utf-8 -*-
"""05_loops_control_flow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17BHQAVcgRpfgffE9IQBkh8B0IhJdPeWm

# **00_guess_my_number**
Problem Statement
Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48
"""

import random

def main():
    print("00_guess_my_number")
    secret_number = random.randint(0, 100)
    print("I am thinking of a number between 0 and 100...")

    while True:
        user_input = input("Enter a guess: ")
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)

        if guess == secret_number:
            print("Congrats! The number was:", secret_number)
            break
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

if __name__ == "__main__":
    main()

"""# **01_fibonacci**

Problem Statement
Write a program to print terms in the Fibonacci sequence up to a maximum value.

In the 13th century, the Italian mathematician Leonardo Fibonacci, as a way to explain the geometric growth of a population of rabbits, devised a mathematical sequence that now bears his name. The first two terms in this sequence, Fib(0) and Fib(1), are 0 and 1, and every subsequent term is the sum of the preceding two. Thus, the first several terms in the Fibonacci sequence look like this:

Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3

Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!). Thus, your program should produce the following sample run:

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
"""

print("01_fibonacci")
max_value = 10000

def main():
    a,b = 0,1
    print(a,b, end =" ")

    while True:
      c = a + b
      if c > max_value:
        break
      print(c, end=" ")
      a, b = b, c


if __name__ == "__main__":
    main()

"""# **02_print_events**
Problem Statement
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

The first even number is 0:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
"""

print("02_print_events")

def main():
  for i in range(20):
    print(i*2)

if __name__ == "__main__":
    main()

"""# **03_wholesome_machine**

Problem Statement
Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

Here's a sample run of the program (user input is in blue):

Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

Note that you can call input() with no prompt and it will still wait for a user to type something!
"""

print("03_wholesome_machine")

correct_affermation = "I am capable of doing anything I put my mind to."

def main():
  print ("welcome to the wholesome Machine")
  while True:
    user_input = input("Please type the following affirmation: ")
    if user_input == correct_affermation:
      print("That's right! :)")
      break
    else:
      print("Hmmm That was not the affirmation.")

if __name__ == "__main__":
    main()

"""Problem Statement
Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

Here's a sample run of the program:

10 9 8 7 6 5 4 3 2 1 Liftoff!
"""

print("04_liftoff")
def main():
    for i in range(10, 0, -1):
      print(i, end = " ")
    print("liftoff")

if __name__ == "__main__":
  main()

"""# **05_double_it**
Problem Statement
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128

Note that:

2 doubled is 4

4 doubled is 8

8 doubled is 16

and so on.

We stop at 128 because that value is greater than 100.

Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:

curr_value = curr_value * 2

This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

while curr_value < 100:
"""

print("05_double_it")

def main():
  user_value = int(input("Enter a number: "))
  while user_value < 100:
      user_value = user_value * 2
      print(user_value)

if __name__ == "__main__":
    main()