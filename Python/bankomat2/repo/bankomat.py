import repo.helpers as helpers


class Atm:
    transaction_string_format = "{0:19} {1:>9} {2:>9}"
    number_of_pin_tries = 3

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.transaction_file = 'transaction.log'
        log = self.open_transaction_log(open_mode='w')  # Open a new transaction log
        log.write('New transaction log created: {0}\n'.format(helpers.get_timestamp()))
        log.close()
        self.add_transaction(balance, balance)

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction(amount, self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            amount = 0

        self.add_transaction(-amount, self.balance)

    def get_balance(self):
        return self.balance

    def calculate_interest(self):
        interest = 2

        if self.balance >= 10001:
            interest = 5
        elif self.balance >= 5001:
            interest = 4
        elif self.balance >= 1001:
            interest = 3

        self.deposit(self.balance * interest)

    def open_transaction_log(self, open_mode='r', encoding='utf-8'):
        return open(self.transaction_file, mode=open_mode, encoding=encoding)

    def add_transaction(self, amount, new_balance):
        log_file = self.open_transaction_log(open_mode='a')
        log_string = '{0} | {1} | {2}\n'.format(helpers.get_timestamp(), str(amount), str(new_balance))
        log_file.writelines(log_string)
        log_file.close()

    def print_transaction_log(self):
        print('\n' + self.transaction_string_format.format("Time", "Amount", "Balance"))
        print(self.transaction_string_format.format("-" * 19, "-" * 9, "-" * 9))

        lines = self.get_a_list_of_transactions()

        for line in range(1, lines.__len__()):
            tmp = lines[line].split(' | ')
            print(self.transaction_string_format.format(tmp[0], tmp[1], tmp[2].strip('\n')))

    def get_a_list_of_transactions(self):
        log_file = self.open_transaction_log()
        lines = log_file.readlines()
        log_file.close()
        return lines

    def call_function(self, function_name, amount):
        method_to_run = getattr(self, function_name, None)

        if method_to_run is not None:
            if amount is None:
                return method_to_run()

            method_to_run(amount)
