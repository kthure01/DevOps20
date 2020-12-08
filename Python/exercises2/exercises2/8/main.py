'''
En maskin som summerar ihop nummer!
'''
class NumberSumMachine():

    def __init__(self):
        self.numbers = []
    
    '''
    Skriv klart funktionen sa att den lagger till ett nummer i self.numbers
    '''
    def add_number(self, number):
        self.numbers.append(number)

    '''
    Skriv klart funktionen sa att den returnerar summan av alla
    nummer i self.numbers
    '''
    def get_sum(self):
        sum = 0
        for x in self.numbers:
            sum += x

        return sum


machine = NumberSumMachine()

machine.add_number(100)
machine.add_number(50)
machine.add_number(50)

sumvalue = machine.get_sum()

'''
Korrekta svaret ska vara

    200
'''
print(sumvalue)
