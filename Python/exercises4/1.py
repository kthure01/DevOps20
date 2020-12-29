def get_numeric_value(text):
    '''
    Gor klart funktionen sa att den endast returnerar det numeriska vardet
    i en strang.
    '''
    return ' '.join([x for x in text if x.isdigit()])


text = 'John has 2 cars'

numeric = get_numeric_value(text)

print(numeric)  # forvantat resultat ar `2`
