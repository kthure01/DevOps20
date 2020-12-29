import json

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def write_to_file(self):
        '''
        Skriv klart funktionen sa att den skriver instansen av klassen
        till en .json fil som en dictionary.

        Hint:   import json
        Hint:   self.__dict__
        '''
        open('fil3.txt', 'w+').write(json.dumps(self.__dict__, indent=4))


person = Person('Sarah', 32)
person.write_to_file()
