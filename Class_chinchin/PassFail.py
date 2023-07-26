passes = 0
failures = 0
for student in range(10):
    result = int(input('Enter result (1=pass,2=fail): '))
    if result == 1:
        passes += 1
    else:
        failures += 1
print('passed: ', passes)
print('failed: ', failures)
if passes > 8:
    print("Bonus to the instructor")
for count in range(2):
    value = int(input("Enter an integer: "))
if value % 2 == 0:
    print(f'{value} is even')
else:
    print(f'{value} is odd')

