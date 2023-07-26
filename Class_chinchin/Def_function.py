def square(num):
    return num ** 2


print(square.__doc__)
print(help(square))

bless = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mass = [4, 5, 7, 9, 4, 3]
print(mass)
new_bless = bless[0:10]
print(new_bless)
bless[11] = "MOYINOLUWA"
print(bless)
print(id(bless))
print(id(bless[7]))
bim = bless + mass
print(bim)
for item in mass:
    print(item)
print(bless[0:10:2])
print(bless[1:11:2])
print(bless[3:10:4])
print(bless[7])
