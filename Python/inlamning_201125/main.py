'''
Inlämningsuppgift Linux och skriptspråk

Täcker kunskapsmål:
7.Använda versionshantering av kod via kommandotolken
8.Skapa Python script

Lämna in en zip av din privata/publika GitHub repo för inlämningsuppgiften på PingPong. Bifoga
även en bild på ditt repo om den är privat (annars en länk).

Detta är en IG/G uppgift

Skapa en simpel miniräknare i Python.
Programmet skall kunna ta in två argument och returnera summan i form av + - * /.

Om summan är 1<50 printa ”Less then fifty”
Om summan är 50 printa ”Fifty”
Om summan är mer än 50 men mindre än 100 ”Almost a hundred”
Om summan är 100 printa ut ”Spot on!”
Om summan är mer än 100 printa ”Missed the spot!”

Använd Git för att verisionshantera koden och ladda upp git-repot till din GitHub

Programmet måste inte vara felfritt eller buggfritt. Framför allt är det verisionshanteringen som testas.
Det skall finnas tre commits under historiken.
'''


def get_sum(x, y):
    return x + y


def get_difference(x, y):
    return x - y


def get_product(x, y):
    return x * y


def get_quotient(x, y):
    return x / y


def check_result(number_to_check):
    message = ''

    if (number_to_check > 1 and number_to_check < 50):
        message = "less than fifty"
    elif (number_to_check == 50):
        message = "Fifty"
    elif (number_to_check > 50 and number_to_check < 100):
        message = "Almost a hundred"
    elif (number_to_check == 100):
        message = "Spot on!"
    else:
        message = "Missed the spot"

    return message


number_one = int(input("Enter number 1: "))
number_two = int(input("Enter number 2: "))

print("Addition: ", check_result(get_sum(number_one, number_two)))
print("Difference: ", check_result(get_difference(number_one, number_two)))
print("Product: ", check_result(get_product(number_one, number_two)))
print("Quotient: ", check_result(get_quotient(number_one, number_two)))
