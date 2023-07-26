student = 0
grade_counter = 0
grade = int(input('Enter grade,and -25 to terminate: '))
while grade != -25:
    student += grade
    grade_counter +=1
    grade = int(input("Enter grade and -25 to terminate: "))
    if grade_counter !=0:
        average = student / grade_counter
        print(f'Class average is {average:.2f}')
    else:
        print('No grades were entered')



