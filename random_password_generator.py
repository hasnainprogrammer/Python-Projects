import random

letters = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r'
,'s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
'P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','%','*','!']
letter = int(input('How Many Letters you Want: '))
digit = int(input('How Many Digits you Want: '))
symbol = int(input('How Many Symbols you Want: '))
password = ''
for char in range(1,letter + 1):
    random_char = random.choice(letters)
    password += random_char
    # print(password) 
for d in range(1,digit + 1):
    random_d = random.choice(digits)
    password += random_d
    # print(password) 
for s in range(1,symbol + 1):
    random_s = random.choice(symbols)
    password += random_s
print(password)
