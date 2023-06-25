#This game is called "Guess the Number." The player has to guess a randomly generated number within a certain range.


import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()



#instructions 
#To run the game in VS Code, follow these steps:

# Open VS Code and create a new Python file. For example, name it guess_the_number.py.

# Copy the code into the file.

# Save the file.

# Open the integrated terminal in VS Code by going to View -> Terminal or using the shortcut Ctrl+ backtick.

# In the terminal, navigate to the directory where you saved the Python file using the cd command. For example, if the file is in the Desktop directory, you can use the command cd Desktop.

# Run the Python file with the command python guess_the_number.py.

# The game will start, and you can play by guessing numbers within the given range. The program will provide feedback if your guess is too high or too low. Once you guess the correct number, it will display the number of attempts you took.
