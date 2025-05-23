# -*- coding: utf-8 -*-
"""00_intro_python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NQzqJqRWmvtjgnik_l_WI67Rm0w640sR

# **01_add_two_numbers**

Problem Statement
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.
"""

print("01_add_two_numbers")

def add():
  print("This application for add two numbers")
  first_number = int(input("Enter your first number: "))
  second_number = int(input("Enter your second number: "))
  total = int(first_number +second_number)
  print(f"The sum of {first_number} and {second_number} is {total}")

if __name__ == "__main__":
    add()

"""# **02_agreement_bot**

Problem Statement
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow!
"""

print("02_agreement_bot")

def bot():
  animal = str(input("What's your favorite animal? "))
  print(f"My favorite animal is {animal} also!")

if __name__ == "__main__":
 bot()

"""# **03_fahrenheit_to_celsius**

Problem Statement
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

(Note. The .0 after the 5 and 9 matters in the line above!!!)

Here's a sample run of the program (user input is in bold italics):

Enter temperature in Fahrenheit: 76

Temperature: 76.0F = 24.444444444444443C
"""

print("03_fahrenheit_to_celsius")

def temp():
  print("This code for converting Fahrenheit to Celsius")
  fahrenheit_degree = float(input("Enter your Fahrenheit_degree "))
  celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
  print(f" Temprature {fahrenheit_degree} F = {celsius_degree}C ")

if __name__ == "__main__":
 temp()

"""# **04_how_old_are_they**

Problem Statement
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
"""

print ("04_how_old_are_they")

def add_ages():
    anton: int = 21  # Anton's age is given as 21 years old
    beth: int = 6 + anton  # Beth is 6 years older than Anton
    chen: int = 20 + beth  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew is as old as Chen plus Anton
    ethan: int = chen  # Ethan is the same age as Chen

    print("Anton is", anton, "years old.")
    print("Beth is", beth, "years old.")
    print("Chen is", chen, "years old.")
    print("Drew is", drew, "years old.")
    print("Ethan is", ethan, "years old.")

if __name__ == "__main__":
  add_ages()

"""# **05_triangle_perimeter**

Problem Statement
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5
"""

print("05_triangle_perimeter")

def triangle():
  print("This code is about the sum of triangle sides")
  side1: float = float(input("Enter the first number of side 1? "))
  side2: float = float(input("Enter the second number of side 2?"))
  side3: float = float(input("Enter is the third number of side 3?"))
  total:float = (side1 + side2 + side3)
  print(f"The perimeter of the triangle is {total}")

if __name__ == "__main__":
  triangle()

"""# **06_square_number.**

Problem Statement
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
"""

print("06_square_number.")

def square():
  print("This code is about the square of number")
  number: float = float(input("Type a number to see its square: "))
  square: float = number * number
  print(f"{number} squared is {square}")

if __name__ == "__main__":
  square()