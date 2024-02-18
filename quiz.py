questions = [
    {'question':'Linus Torvalds created linux.(True/False)','answer':'true'},
    {'question':'DOS was the first operating system.(True/False)','answer':'true'},
    {'question':'HTML is a programming language.(True/False)','answer':'false'},
    {'question':'OSI Model is a physical model.(True/False)','answer':'false'},
    {'question':'Linked lists is a linear data structure.(True/False)','answer':'true'},  
    {'question':'Tree is a linear data structure.(True/False)','answer':'false'},  
]


question_number = 0
score = 0
for question in questions:
    question_text = question['question']
    question_answer = question['answer']
    question_number += 1
    guess = input(f'Q.{question_number}: {question_text}: ').lower()
    if guess == question_answer:
        print(f'You got it right! The correct answer was {question_answer}.')
        score += 1
        print(f'Your Score is: {score}/{question_number}')
        print('\n')
    else:
        print(f'You guess it wrong! The correct answer was {question_answer}.')
        print(f'Your Score is: {score}/{question_number}')
        print('\n')

print(f'Your final score is: {score}/{len(questions)}')


     
    
