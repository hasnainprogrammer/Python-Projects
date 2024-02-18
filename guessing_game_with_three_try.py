import random

print('\n______ Guessing Game _____\n')
print("* You have three Try's to Guess the Correct Number:\n")
correct_number = random.randint(1,10)
guess_try = 0
while guess_try < 3:
    guess = int(input('Guess the number:  '))
    guess_try +=  1
    if(guess == correct_number):
        print('You Won!')
        break
else:
    print('Oops! You Failed to Guess the Number Correctly')