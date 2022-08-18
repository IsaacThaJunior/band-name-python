# Step 4

import random
from hangman_words import word_list
from hangman_art import logo, stages

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

print(logo)

# Create blanks
display = []
print(f'The chosen word is {chosen_word}')
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in chosen_word:
        print(f'You have already guessed {guess}.')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'{guess} is not in the word. Therefore you lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])
