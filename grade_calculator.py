def grade_calculator():
    subject1 = int(input('Enter Marks in Subject1: '))
    subject2 = int(input('Enter Marks in Subject2: '))
    subject3 = int(input('Enter Marks in Subject3: '))
    subject4 = int(input('Enter Marks in Subject4: '))
    subject5 = int(input('Enter Marks in Subject5: '))
    subject6 = int(input('Enter Marks in Subject6: '))
    total = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
    percentage = total / 600 * 100
    print(f"You Got {total} Marks Out Of 600")
    print(f"And Your Percentage is {percentage}")
    if percentage <= 50:
        print("And Your Grade is C")
    elif percentage > 50 and percentage < 70:
        print("And Your Grade is B")
    elif percentage > 70 and percentage < 80:
        print("And Your Grade is A")
    elif percentage > 80 and percentage <= 100:
        print("And Your Grade is A+")
    else:
        print('Invalid')


grade_calculator()

