# Skriv ett Python-program för att hitta de upprepade objekten i en tupel

tuple_one = ("ett", "två", "tre", "ett", "två", "fyra", "tre", "fem")

set_one = set(tuple_one)

found = []
unik = []

for item in tuple_one:
    if item not in found:
        found.append(item)
    else:
        unik.append(item)

print(found)
print("Dubletter ", unik)