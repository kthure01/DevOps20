'''
Skriv klart funktionen sa att den returnerar False om numret inte
ar delbart med 2, annars True.

Hint:

    anvand modulo operatorn `%`

'''
def is_divisible_by_two(number):
    return number % 2 == 0


'''
Ska vara True
'''
print(is_divisible_by_two(4))


'''
Ska vara False
'''
print(is_divisible_by_two(3))
