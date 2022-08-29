# import random
# # Number Guessing Game
# the_choice = random.choice(range(1, 101))
# choice = input("Choose a difficulty. Type 'Easy' or 'Hard': ")

# if choice == "Easy":
#     number_of_lives = 10
#     print(f'you have {number_of_lives} lives to guess the number')
#     while number_of_lives > 0:
#         guess = int(input("Guess a number: "))
#         if guess == the_choice:
#             print("You win!")

#         elif guess > the_choice:
#             print("Too high")
#             number_of_lives -= 1
#             print(f'You have {number_of_lives} lives to guess the number')
#         elif guess < the_choice:
#             print("Too low")
#             number_of_lives -= 1
#             print(f'You have {number_of_lives} lives to guess the number')
# if choice == "Hard":
#     number_of_lives = 5
#     print(f'you have {number_of_lives} lives to guess the number')
#     while number_of_lives > 0:
#         guess = int(input("Guess a number: "))
#         if guess == the_choice:
#             print("You win!")
#             break
#         elif guess > the_choice:
#             print("Too high")
#             number_of_lives -= 1
#             print(f'You have {number_of_lives} lives to guess the number')
#         elif guess < the_choice:
#             print("Too low")
#             number_of_lives -= 1
#             print(f'You have {number_of_lives} lives to guess the number')

# Angela's solution
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

