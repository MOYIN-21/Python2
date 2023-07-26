number = 89746
integer = 0
for M in range(5):
    digit = number % 10
    number =(number // 10)
    print(digit,end=" ")
