import pandas as pd

names = []
payments = []
how_many = int(input('What number of data you will be Entering: '))
for i in range(how_many):
    name = input('Enter Name: ')
    payment = input('Enter Payment: ')
    names.append(name)
    payments.append(payment)
    d = { 
        'name':names,
        'payment':payments
    }
    df = pd.DataFrame(d)
print('\n')
print('--- Your all Entered prices ---')
print('\n')
print(df)
total_list = []
total = 0
for j in df['payment']:
   total_list.append(j)
for t in total_list:
    total += int(t)
print('\n')
print('--------------------------')
print(f'Total Amount is: {total}')
print('--------------------------')

