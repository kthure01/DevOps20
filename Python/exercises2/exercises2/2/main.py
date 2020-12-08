class BankAccount():

    def __init__(self):
        self.money = 1600

    def get_money(self):
        return self.money

    '''
    Gor klart den har funktionen,
    den ska oka vardet pa self.money med vardet som skickas in.
    '''
    def add_money(self, amount):
        self.money += amount


mitt_konto = BankAccount()
mitt_konto.add_money(198)


'''
Det korrekta svaret i denna print ska vara:

    1798
'''
print(mitt_konto.get_money())
