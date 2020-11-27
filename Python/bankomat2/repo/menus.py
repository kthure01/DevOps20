class Menu():
    def __init__(self, menu):
        self.menu_items = menu
        self.users_choice = -1

    def print_menu(self):
        for item in self.menu_items:
            if item[0] == 0: continue
            print(f"{item[0]}) {item[1]}")

    def get_menu_size(self):
        return len(self.menu_items) - 1  # Skip Dummy item

    def get_user_input(self):
        user_choice = input(f"Enter your choice [{self.menu_items[0][0] + 1}-{self.get_menu_size()}]: ")

        self.users_choice = int(user_choice) if self.validate_input(user_choice) else -1
        print()

    def validate_input(self, user_choice):
        is_valid = False

        if not user_choice.isdigit():
            is_valid = False
        elif int(user_choice) >= self.menu_items[0][0] and int(user_choice) <= self.get_menu_size():
            is_valid = True

        return is_valid

    def get_function_to_run(self):
        return self.menu_items[self.users_choice][2]
