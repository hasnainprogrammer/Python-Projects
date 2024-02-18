def calculator():
    first_number = int(input('Enter First Number: '))
    operator = str(input('Enter Operator: '))
    second_number = int(input('Enter Second Number: '))
    if operator == '+':
        print(f'Sum is = {first_number + second_number}')
    elif operator == '-':
        print(f'Subtraction is = {first_number - second_number}')
    elif operator == '*':
        print(f'Product is = {first_number * second_number}')
    elif operator == '/':
        print(f'Division is = {first_number / second_number}')
    else:
        print('Please Enter Valid Value')


calculator()
