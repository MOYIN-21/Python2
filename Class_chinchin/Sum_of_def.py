number = [10, 20, 30, 40, 50]
sums = 0
for lists in number[0:]:
    sums += lists
print(sums)

number = [10, 20, 30, 40, 50]
sums = 0
for lists in number[0:: 2]:
    sums += lists
print(sums)

number = [10, 20, 30, 40, 50]
sums = 0
for lists in number[1:: 2]:
    sums += lists
print(sums)

number = [10, 20, 30, 40, 50]
for lists in range(len(number)):
    number[lists] = number[lists] ** 2
print(number)





