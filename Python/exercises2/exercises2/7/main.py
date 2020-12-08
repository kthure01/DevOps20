'''
Skriv klart funktionen sa att den returnerar forsta vardet i en tuple.
'''
def get_first_element_in_tuple(tup):
    return tup[0]


my_tuple = (68, 42)

first = get_first_element_in_tuple(my_tuple)


'''
Korrekta svaret ska vara

    68
'''
print(first)
