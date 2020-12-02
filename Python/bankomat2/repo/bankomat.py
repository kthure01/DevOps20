import repo.helpers


class Atm:

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.transaction_log = []
        self.old_balance = 0
        self.add_transaction("+", balance)

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction("+", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.add_transaction("-", amount)

    def get_balance(self):
        return self.balance

    def collect_interest(self):
        interest = 2

        if self.balance >= 10001:
            interest = 5
        elif self.balance >= 5001:
            interest = 4
        elif self.balance >= 1001:
            interest = 3

        self.old_balance = self.balance
        self.balance *= interest
        self.add_transaction("+", self.balance - self.old_balance)

    def add_transaction(self, sign, amount):
        self.transaction_log.append((repo.helpers.get_timestamp(), sign, amount, self.balance))

    def print_log(self):
        print("\n{0:8} {1:^3} {2:>9} {3:>9}".format("time", "+/-", "amount", "balance"))
        print("{0} {1} {2} {3}".format("-" * 8, "-" * 3, "-" * 9, "-" * 9))

        for item in self.transaction_log:
            print("{0:8} {1:^3} {2:>9} {3:>9}".format(item[0], item[1], item[2], item[3]))

    def call_function(self, function_name, amount):
        method_to_run = getattr(self, function_name, None)

        if method_to_run is not None:
            if amount is None:
                return method_to_run()

            method_to_run(amount)
