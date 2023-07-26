def Multiplication_table(num):
    for M in range(1, 13):
        for O in range(1, num + 1):
            print('%i X %i = %-4i' % (O, M, O * M), end='\t\t')
        print()


Multiplication_table(12)
