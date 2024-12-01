#  this is program is asking for numbee of program and number of test per studet

#  get the number of student
num_student = int(input("How many student do you have ?" ))

# get the number of test
num_test_score = int(input("How many test score per student ? "))

#  Determine each student test score
for student in range(num_student):
#  initialize an accumulator
    total = 0.0

#   Display the student number
    print(f'Student number is {student + 1}')
    print('---------------')

#   get the student's scores
    for test_num in range(num_test_score):
        print(f' test number is {test_num + 1}', end=''3)
        score = float(input(':'))

        #  add score to accumelator
        total += score

    average = total/num_test_score


    print(f'the average for studet number {student + 1} ' f'is {average: .1f}')
    print()