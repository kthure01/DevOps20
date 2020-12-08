# Denna funktion ska oppna "input.txt" och returnera innehallet.
def get_contents_from_file(in_file):
    file_opend = open(in_file)
    return file_opend.read()


contents = get_contents_from_file("input.txt")
print(contents)

'''
Det korrekta svaret som printas ut ska vara:

    Jag kan Python!
'''
