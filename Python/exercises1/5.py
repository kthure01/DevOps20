# Skriv ett Python-program för att lägga till ett objekt i en tuple

tuple_one = ("ett", "två")

list_one = list(tuple_one)
list_one.append("tre")

tuple_one = tuple(list_one)

print(tuple_one)
