import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
discriminant = (b * b) - (4 * a * c)
r1 = (-b + math.pow(discriminant, 0.5)) / (2 * a)
r2 = (-b - math.pow(discriminant, 0.5)) / (2 * a)

if discriminant > 0:
    print("The equation has two roots", r1, r2)
elif discriminant < 0:
    print("The equation has no real root", r1)
else:
    0 == discriminant
    print("The equation has one roots")

