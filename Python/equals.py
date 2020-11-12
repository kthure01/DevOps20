''' Equals
Write an app that read two integers from the user and 
checks whether they are equal or not. 
When printing output print the numbers and if they are
equal for example “1 and 2 are not equal”

Example output:
1 and 2 are not equal
'''
def app_equals():
    number_1 = int(input("Ange nummer 1: "))
    number_2 = int(input("Ange nummer 2: "))

    if number_1 == number_2:
        print("Numren är lika")
    else:
        print("Numren är olika")

# app_equals()


''' Positive or negative
Write an app that reads a number and determines if it is
positive or negative
Example data:
-1
Example output
-1 is negative
'''
def app_positive_negative():
    number = int(input("Ange ett nummer: "))

    if number < 0:
        print("Numret är negativt")
    else:
        print("Numret är positivt")

# app_positive_negative()


''' Even or odd
Determine whether a number is even or odd. The number should be given by the 
user as input. When printing the output, it must contain the numbers and the 
result where result is either “even” or “odd”.
• Tips. Use the modulu operator, all even numbers are divisible by two, 
no uneven number is divisible by two
Example data:
5
Example output:
The number 5 is odd
'''
def app_even_or_odd():
    number = int(input("Ange ett nummer: "))

    msg = "jämt" if number % 2 == 0 else "ojämt"
    print(f"Nummer {number} är {msg}")

# app_even_or_odd()

'''Multiples
Write an app that reads two integers from the user and determines whether the first is a multiple of
the second and displays the result.
Example data:
5
20
Example output:
5 is a multiple of 20
'''
def app_multiples():
    number_1 = int(input("Ange nummer 1: "))
    number_2 = int(input("Ange nummer 2: "))
    
    if number_2 % number_1 == 0:
        print(f"Nummer {number_1} är en multipel av {number_2}")
        
# app_multiples()

'''Comparing numbers
Write an app that asks the user to enter two numbers, obtains them from the user and displays the
larger number followed by the words "is larger". If the numbers are equal, display the
message "These numbers are equal”
Example data:
2
4
Example output:
4 is larger
'''

def app_comparing_numbers():
    number_1 = int(input("Ange nummer 1: "))
    number_2 = int(input("Ange nummer 2: "))
    
    if number_1 == number_2:
        print("Numren är lika")
    elif number_1 > number_2:
        print(f"Nummer {number_1} är större")
    else:
        print(f"Nummer {number_2} är större")

# app_comparing_numbers()

'''Quadrant
Write an app that reads a coordinate point in a XY coordinate system and 
determines in which quadrant that point lies.
Example data:
X = 7
Y = 9
Example output:
The point (7,9) lies in the First quadrant
'''
def app_quadrant():
    x = int(input("Ange x: "))
    y = int(input("Ange y: "))
    
    if x > 0 and y > 0:
        q = 1
    elif x > 0 and y < 0:
        q = 4
    elif x < 0 and y > 0:
        q = 2
    elif x < 0 and y < 0:
        q = 3
    else:
        q = 0
    
    if q >= 1 and q <= 4:
        print(f"Punkten ({x},{y}) ligger i kvadrant {q}")
    else:
        print(f"Punkten ({x},{y}) ligger i origo")

# app_quadrant()

'''Weekday
Write an app that read a number from the user and outputs the corresponding weekday. Monday is
day 1.
• If you have checked all valid numbers, you can assume the rest are invalid
Example data:
2
Example output:
Tuesday
'''
def app_weekday():
    week_days = ({
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thirsday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
        })
    number = int(input("Ange ett nummer: "))
    
    if number < 1 or number > 7:
        print("Fel nummer")
        return -1
    
    print(f"Nummer {number} motsvarar {week_days[number]}")

# app_weekday()

'''Leap year
Write an app that takes a year as input and checks whether it is a leap year. When printing output include the given year and the result
• A leap year is divisible by 4 and not divisible by 100
• A leap year is divisible by 4 and divisible by 400
• 1900 is not a leap year despite being divisible by 4 because it is also divisible by 100
• 2000 is a leap year because it is divisible by 4 and divisible by 400 despite also being divisible by 100
Example data:
2000
Example output:
The year 2000 is a leap year

These extra days occur in each year which is an integer multiple of 4
(except for years evenly divisible by 100, which are not leap years unless evenly divisible by 400).
'''

def app_leap_year(year):
    leap_year = False
    
    if year % 4 == 0:
        leap_year = True

        if year % 100 == 0 and year % 400 != 0:
            leap_year = False

    print(f"{year} är {leap_year}") 
    return leap_year     

# app_leap_year(2000)    


    
    

