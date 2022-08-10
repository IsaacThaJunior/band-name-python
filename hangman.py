# Create a hangman game
import random

word_list = ['ardvard', 'baboon', 'camel']

choice = random.choice(word_list)

print(f'The chosen word is {choice}')

guess = input('Guess a letter: ')

display = []
for i in range(len(choice)):
    display.append('_')

for position in range(len(choice)):
    letter = choice[position]
    if guess == letter:
        display[position] = letter

print(display)