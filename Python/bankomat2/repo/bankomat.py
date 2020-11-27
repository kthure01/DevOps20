class Cash_machine():

    def __init__(self, pin, balance):
        self.valid_pin_length = [4, 6]
        self.pin_tries = 3
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

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

        self.balance *= interest

    def get_pin(self):
        n = self.pin_tries
        while n > 0:
            try:
                # pin = int(input("Enter your pin, 4 or 6 digits: "))
                pin = int(input("Enter your pin, 4 or 6 digits: ") or self.pin)  # FOR TESTING ONLY

                if self.validate_pin(pin):
                    return True

                n -= 1
                print(f"ERROR: Invalid pin! {n} tries left")
            except:
                n -= 1
                print(f"ERROR: Invalid pin! {n} tries left")

    def validate_pin(self, pin):
        valid = False

        if self.pin == pin:
            valid = True
        elif len(str(pin)) not in self.valid_pin_length:
            valid = False

        return valid
