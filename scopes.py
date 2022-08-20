import random
# Number Guessing Game
the_choice = random.choice(range(1, 101))
choice = input("Choose a difficulty. Type 'Easy' or 'Hard': ")

if choice == "Easy":
    number_of_lives = 10
    print(f'you have {number_of_lives} lives to guess the number')
    while number_of_lives > 0:
        guess = int(input("Guess a number: "))
        if guess == the_choice:
            print("You win!")
            break
        elif guess > the_choice:
            print("Too high")
            number_of_lives -= 1
            print(f'You have {number_of_lives} lives to guess the number')
        elif guess < the_choice:
            print("Too low")
            number_of_lives -= 1
            print(f'You have {number_of_lives} lives to guess the number')
if choice == "Hard":
    number_of_lives = 5
    print(f'you have {number_of_lives} lives to guess the number')
    while number_of_lives > 0:
        guess = int(input("Guess a number: "))
        if guess == the_choice:
            print("You win!")
            break
        elif guess > the_choice:
            print("Too high")
            number_of_lives -= 1
            print(f'You have {number_of_lives} lives to guess the number')
        elif guess < the_choice:
            print("Too low")
            number_of_lives -= 1
            print(f'You have {number_of_lives} lives to guess the number')

