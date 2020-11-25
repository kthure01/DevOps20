# Skriv ett Python-program för att konvertera en tuple till en sträng.

tuple_one = ("ett", "två", "tre")

lista_ett = list(tuple_one)

string_one = ' '.join(map(str,lista_ett))

print(string_one)
