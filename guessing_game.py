import random

random_number = random.randint(1,10)
guess_number = int(input('Guess the Number: '))
if guess_number == random_number:
    print('Congratulation! You Won')
else:
    print(f'Oops! You Loss The Correct Number is {random_number}')
