# Importing the modules
import random
from hangman_art import stages, logo  # import stages and logo from hangman_art module
from hangman_word import word_list  # import word_list from hangman_word module

# Print the hangman logo
print(logo)

# Choose a random word from the list
chosen_word = random.choice(word_list)

# Get the length of chosen_word
length = len(chosen_word)

# Initializing the empty list named 'display'
display = []

# Initializing the lives variable to 6, this is the total no. of lives 
lives = 6

# Append an underscore for each letter in the chosen word
for _ in range(length):
    display.append("_")

# Set game_on to True to start the game loop
game_on = True
while game_on:
    # Get the user's guess
    guess = input("Guess a letter: ").lower()

    # Iterate through each letter in the chosen word
    for pos in range(length):
        letter = chosen_word[pos]
        # If the user's guess is correct, update the display list
        if letter == guess:
            display[pos] = letter

    # If the user's guess is not in the chosen word, decrement the lives variable
    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed {guess}, that's not a word. You lose a life.")
    # Print the current state of the word
    print(" ".join(display))

    # If all letters have been correctly guessed, end the game loop
    if "_" not in display:
        game_on = False
        print("You win.")

    # If the user has no more lives, end the game loop
    if lives == 0:
        game_on = False
        print(f"The word was {chosen_word}, You Lose.")

    # Print the current stage of the hangman drawing
    print(stages[lives])
