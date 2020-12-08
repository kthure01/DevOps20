'''
Gor klart den har funktionen sa att den skriver ut
summan av x och y, till en fil.
'''
def write_sum_to_file(x, y, filename):
    out_file = open(filename, 'w+')
    out_file.write(str(x + y))


write_sum_to_file(10, 30, "sum.txt")
'''
Filen ska nu innehalla:

    40
'''
