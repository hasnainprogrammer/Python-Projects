import random
random_num = random.randint(0,1)
guess_toss = int(input("Select Head or Tail? (1) for Head , (2) for Tail:  "))
if guess_toss == random_num:
    print('You Won!')
else:
    print('You Loss!')
