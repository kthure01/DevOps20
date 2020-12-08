mydict = {
    "name": "Albert",
    "age": 37
}


'''
Skriv klart funktionen sa att den andrar "name" pa en dictionary
'''
def change_name(dict_object, new_name):
    dict_object['name'] = new_name


change_name(mydict, "Sarah")
print(mydict["name"])


'''
Det korrekta svaret fran print ska vara:

    Sarah
'''
