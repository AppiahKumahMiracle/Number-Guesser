from colors import *
from random import randint

# welcome Screen Message
print(BLUE, '******** Welcome To Your World Of Guessing Game ********')
user_select = int(input(WHITE + 'Choose Your Level\n'
                                '1. Normal (1 - 50)\n'
                                '2. Intermediate (1 - 200)\n'
                                '3. Hard (1 - 500)\n'
                                '4. Exit Application\n\n'
                                'Enter Request: '))

# user's Option
guess_range = 0
if user_select == 1:
    guess_range = 50
elif user_select == 2:
    guess_range = 200
elif user_select == 3:
    guess_range = 500
elif user_select == 4:
    print('******** Thanks for passing by...********\n'
          '******** Hope To See You Again ********')
    exit(1)
else:
    print(RED, 'Invalid Request...Try Again')

# Generate random number between certain range
generator = randint(1, guess_range)

# user chances
user_chance = 4
# Accepting the user input and validation, if it matches the generated.
for i in range(4):
    user_guess = int(input(WHITE + 'Provide Your Guess Number: '))

    if user_guess == generator:
        print(GREEN, 'Hurray!!!...You Guess it Correct')
        break
    elif user_guess > generator:
        print(YELLOW, 'Your Guess Is Too High, Try Again')

    elif user_guess < generator:
        print(YELLOW, 'Your Guess Is Too Low, Try Again')

    user_chance = user_chance - 1
    print(f'Number Of chances Left is {user_chance}')

# inform user of the correct guess number
if user_chance == 0:
    print(RED, f'Sorry the Correct Guess is {generator}')


