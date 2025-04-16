import random
  
stages = ['''
    ****************
    |               |
    |
    |
    |
    |
    ****************
    ***''' ,'''
    ***
    ****************
    |               |
    |               0
    |               |
    |
    |
    *****************
    *** ''', '''
    ***
*************
    |               |
    |               0
    |              /|
    |
    |
    *****************
     *** ''', '''
    ****************
    |               |
    |               0
    |              /|\\
    |
    |
    *****************
     *** ''', '''
    ****************
    |               |
    |               0
    |              /|\\
    |              /
    |
    *****************
     *** ''', '''
    ****************
    |               |
    |               0
    |              /|\\
    |              / \\
    |
    *****************
     *** ''']
            
words = ["apple", "banana", "graps", "orange"]
        
chosen_word = random.choice(words).lower()
word_display = ['_' for _ in chosen_word]
guess_letters = []
lives = len(stages) - 1

print("Welcome to the Hangman")
print("Guess the fruits word.")

while True:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid letter.")
        continue

    if guess in guess_letters:
        print("You already guessed this letter, please choose a different one.")
        continue

    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good Guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) - lives - 1])
        lives -= 1
        print(f"You have {lives} lives left.")
    
    if "_" not in word_display:
        print("\nCongratulations! You guessed the word:", chosen_word)
        break

    if lives == 0:
        print("\nYou lose! The word was:", chosen_word)
        print(stages[-1])
        break
