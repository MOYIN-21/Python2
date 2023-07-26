number = int(input("Enter any 5 integer: "))
for M in range(5):
    digit = number % 10
    number =(number // 10)
    print(digit,end=" ")


