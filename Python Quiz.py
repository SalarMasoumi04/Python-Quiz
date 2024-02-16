print('Welcome to Python Quiz')
answer=input('Are you ready to play the Quiz ?')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer=input('Question 2: Do you follow any author on Python Quiz? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: What is the name of your favorite website for learning Python?')
    if answer.lower()=='python.org':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thank you for Playing Python Quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Have a Great Time')
