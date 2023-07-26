def sum1(n):
    total = 0
    for counter in range(1, n + 1):
        total += counter
        print(total)


sum1(5)


def greater(num1, num2):
    maximum = num1
    if num2 > num1:
        maximum = num2
    return maximum


print(greater(14, 6, ))


def smaller(num1, num2, num3, num4):
    maximum = num1
    if num2 > num1:  # and num2 < num3 and num2 < num4:
        maximum = num2
    if num3 > num1:  # and num3 < num2 and num3 < num4:
        maximum = num3
    if num4 > num1:
        # and num4 < num2 and num4 < num3:
        maximum = num4
    print(maximum)
    minimum = num1
    if num2 < num1:  # and number2 > number3 and number2 > number4:
        minimum = num2
    if num3 < num2:  # and number3 > number1 and number3 > number4:
        minimum = num3
    if num4 < num3:  # and number4 > number1 and number4 > number2:
        minimum = num4
    print(minimum)


smaller(40, 11, 983, 52)

# def greater(number1, number2, number3, number4):
#     minimum = number1
#     if number2 < number1:  # and number2 > number3 and number2 > number4:
#         minimum = number2
#     if number3 < number2:  # and number3 > number1 and number3 > number4:
#         minimum = number3
#     if number4 < number3:  # and number4 > number1 and number4 > number2:
#         minimum = number4
#     return (minimum)
# print(greater(855, 914, 500, 950))
