numbers = [
    349,
    319,
    5,
    971,
    4,
    97,
    3,
    1,
    20,
    508,
    47
]

'''
Just nu printar loopen ut alla nummer i listan.
Vi vill att den bara ska printa ut nummer som ar jamt delbara med 2.

Korrekta svaret ska vara:

    4
    20
    508
'''
for x in numbers:
    if x % 2 == 0:
        print(x)

