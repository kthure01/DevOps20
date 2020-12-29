'''
Write a program that prints the numbers from 1 to 100
and for multiples of ‘3’ print “Fizz” instead of the number
and for the multiples of ‘5’ print “Buzz”.
'''


def fizzbuzz():
    cnt = 1
    for x in range(1, 101):
        cnt += 1
        if x % 3 == 0 and x % 5 == 0:
            x = 'FizzBuzz'
        elif x % 3 == 0:
            x = 'Fizz'
        elif x % 5 == 0:
            x = 'Buzz'

        if cnt < 10:
            print(x, end=', ')
        else:
            print(x, end=',\n')
            cnt = 0

fizzbuzz()

# forvantat resultat
'''
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26,
Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...
'''
