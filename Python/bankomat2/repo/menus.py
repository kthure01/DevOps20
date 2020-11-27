class Menu():
    def __init__(self, menu):
        self.items = {}
        self.users_choice = None

        for n, item in enumerate(menu, start=1):
            self.items[n] = item

    def print_menu(self):
        for item in self.items.items():
            print(f"{item[0]}) {item[1]}")

    def get_menu_size(self):
        return len(self.items)

    def get_user_input(self):
        self.users_choice = input(f"Enter your choice [1-{self.get_menu_size()}]: ")

    def validate_input(self):
        pass
