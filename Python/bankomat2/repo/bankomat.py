import repo.helpers


class Cash_machine():

    def __init__(self, pin, balance):
        self.valid_pin_length = [4, 6]
        self.pin_tries = 3
        self.pin = pin
        self.balance = balance
        self.loggbook = []
        self.input_amount = 0
        self.old_balance = 0
        self.add_to_log("+")

    def deposit(self):
        self.balance += self.input_amount
        self.add_to_log("+")

    def withdraw(self):
        if self.balance >= self.input_amount:
            self.balance -= self.input_amount
            self.add_to_log("-")

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
        self.input_amount = self.balance - self.old_balance
        self.add_to_log("+")

    def get_pin(self):
        n = self.pin_tries
        while n > 0:
            # pin = input("Enter your pin, 4 or 6 digits: ")
            pin = input("Enter your pin, 4 or 6 digits: ") or self.pin  # FOR TESTING ONLY

            if self.validate_pin(pin):
                return True

            n -= 1
            print(f"ERROR: Invalid pin! {n} tries left")

    def validate_pin(self, pin):
        is_valid = False

        if not pin.isdigit():
            is_valid = False
        elif len(str(pin)) not in self.valid_pin_length:
            is_valid = False
        elif self.pin == pin:
            is_valid = True

        return is_valid

    def add_to_log(self, sign):
        self.loggbook.append((repo.helpers.get_timestamp(), sign, self.input_amount, self.balance))

    def print_log(self):
        for item in self.loggbook:
            print(f"{item[0]} {item[1]} {item[2]:6} {item[3]:6}")

    def call_function(self, function_name, amount):
        self.input_amount = int(amount)

        method_to_run = getattr(self, function_name, None)

        if method_to_run is not None:
            method_to_run()
