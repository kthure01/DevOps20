import time

import repo.bankomat as bankomat
import repo.menus as menus
from repo.helpers import Helpers

# Lite globala variabler
number_of_pin_tries = 3
valid_pin_length = [4, 6]
pin_code_for_testing = '2345'
balance_for_testing = 103_024

# Lista för huvudmenyn
# Numrering, Text som skrivs ut, Metod som är kopplad till menyvalet
main_menu_repo = [
    [0, "Main menu: Select what you want to do.", "Not-in-use"],
    [1, "Deposit money", "deposit"],
    [2, "Withdraw money", "withdraw"],
    [3, "Check balance", "get_balance"],
    [4, "Collect interest", "calculate_interest"],
    [5, "Print log", "print_transaction_log"],
    [6, "End program", "end"],
]


def get_pin_code(atm):
    while atm.number_of_pin_tries > 0:
        pin = input(f"Enter your pin, 4 or 6 digits (hint for testing: {atm.pin}): ")

        if validate_pin_code(atm, pin):
            return True

        atm.number_of_pin_tries -= 1
        print(f"ERROR: Invalid pin! You have {atm.number_of_pin_tries} tries left")

    return False


def validate_pin_code(atm, pin):
    is_valid = False

    if not pin.isdigit():
        is_valid = False
    elif len(pin) not in valid_pin_length:  # Kollar längden på pin mot en lista med värden
        is_valid = False
    elif atm.pin == int(pin):
        is_valid = True

    return is_valid


def ask_for_input(atm, menu_action, message):
    if message is None:
        amount = None
    else:
        amount = get_input_as_integer(message)

        if amount is None:
            print("ERROR: >>> No valid input! <<<")
            return

    return atm.call_function(menu_action.get_function_to_run(), amount)


def get_input_as_integer(message):
    try:
        return int(input("\n" + message))
    except ValueError:
        print("ERROR: >>> No integer <<<")
        return None


def print_new_balance(atm):
    print(f"New balance: {atm.get_balance()}")


def main():
    new_atm = bankomat.Atm(int(pin_code_for_testing), balance_for_testing)
    main_menu = menus.Menu(main_menu_repo)

    Helpers().clear()
    print("Welcome to the bank of Zeros and Ones")

    if not get_pin_code(new_atm):
        print("\nERROR: >>> No valid pin <<<")
        print("Exit the program...")
        exit(1)

    while True:
        Helpers().clear()
        main_menu.print_menu()
        main_menu.get_user_input()

        if main_menu.users_item_choice is None:
            print("\nSorry! >>> Wrong choice <<<")
            time.sleep(1)
            continue

        if main_menu.get_menu_item_number() == 1:
            ask_for_input(new_atm, main_menu, "Enter amount to deposit: ")
            print_new_balance(new_atm)

        elif main_menu.get_menu_item_number() == 2:
            ask_for_input(new_atm, main_menu, "Enter amount to withdraw: ")
            print_new_balance(new_atm)

        elif main_menu.get_menu_item_number() == 3:
            print(f"\nCurrent balance is: {new_atm.get_balance()}")

        elif main_menu.get_menu_item_number() == 4:
            print(f"\n{main_menu.users_item_choice[1]}")
            ask_for_input(new_atm, main_menu, None)
            print_new_balance(new_atm)

        elif main_menu.get_menu_item_number() == 5:
            print("\nTransaction records:", end='')
            new_atm.print_transaction_log()

        elif main_menu.get_menu_item_number() == 6:
            print("\nExit the program...")

            exit(0)

        input("Press ENTER to continue")


if __name__ == '__main__':
    main()
