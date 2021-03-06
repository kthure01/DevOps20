"""
# Lista med tuples för huvudmenyn
# Numrering, Text som skrivs ut, Metod som är kopplad till menyvalet
main_menu_repo = [
    (0, "Main menu: Select what you want to do.", "n/a"),
    (1, "Deposit money", "deposit"),
    (2, "Withdraw money", "withdraw"),
    (3, "Check balance", "get_balance"),
    (4, "Collect interest", "calculate_interest"),
    (5, "Print log", "print_transaction_log"),
    (6, "End program", "end"),
]
"""


class Menu:
    def __init__(self, menu):
        self.menu_items = menu
        self.users_item_choice = ''

    def print_menu(self):
        print(f"{self.menu_items[0][1]}")
        for item in self.menu_items:
            if item[0] > 0:
                print(f"{item[0]:2}) {item[1]}")

    def get_menu_size(self):
        return len(self.menu_items) - 1  # Skippar Dummy-raden

    def get_user_input(self):
        user_choice = input(f"Enter your choice ({self.menu_items[1][0]}-{self.get_menu_size()}) [6]: ") or "6"

        if self.validate_input(user_choice):
            self.users_item_choice = self.menu_items[int(user_choice)]
        else:
            self.users_item_choice = None

    def validate_input(self, user_choice):
        if not user_choice.isdigit():
            return False
        elif 0 < int(user_choice) <= self.get_menu_size():
            return True
        else:
            return False

    def get_menu_item_number(self):
        return int(self.users_item_choice[0])

    def get_function_to_run(self):
        return self.users_item_choice[2]
