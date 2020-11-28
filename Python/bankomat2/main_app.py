import time

import repo.bankomat
import repo.helpers
import repo.menus

# Lite globala variabler
number_of_pin_tries = 3
valid_pin_length = [4, 6]
pin_code_for_testing = '2345'
balance_for_testing = 103_024
atm = None
menu_action = None

# Lista med tuples för huvudmenyn
# Numrering, Text som skrivs ut, Metod som är kopplad till menyvalet
main_menu_repo = [
    (0, "Dummy", "Dummy"),
    (1, "Deposit money", "deposit"),
    (2, "Withdraw money", "withdraw"),
    (3, "Check balance", "get_balance"),
    (4, "Collect interest", "collect_interest"),
    (5, "Print log", "print_log"),
    (6, "End program", "end"),
]


def get_pin(atm):
    global number_of_pin_tries

    while number_of_pin_tries > 0:
        pin = input(f"Enter your pin, 4 or 6 digits (hint for testing: {atm.pin}): ")
        # pin = input("Enter your pin, 4 or 6 digits: ") or pin_code_for_testing  # FOR TESTING ONLY

        if validate_pin(atm, pin):
            return True

        number_of_pin_tries -= 1
        print(f"ERROR: Invalid pin! {number_of_pin_tries} tries left")

    return False


def validate_pin(atm, pin):
    is_valid = False

    if not pin.isdigit():
        is_valid = False
    elif len(pin) not in valid_pin_length:  # Kollar längden på pin mot en lista med värden
        is_valid = False
    elif atm.pin == int(pin):
        is_valid = True

    return is_valid


def cash_machine_setup():
    return repo.bankomat.Atm(int(pin_code_for_testing), balance_for_testing)


def prepare_menus():
    return repo.menus.Menu(main_menu_repo)


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


def main():
    global atm, menu_action  # Gör dessa globala för att kunna ändras i metoderna
    atm = cash_machine_setup()
    menu_action = prepare_menus()

    repo.helpers.clear()
    print("Welcome to the bank of Zeros and Ones")

    if not get_pin(atm):
        print("\nERROR: >>> No valid pin <<<")
        print("Exit the program...")
        exit(1)

    continue_to_run = True
    while continue_to_run:
        repo.helpers.clear()
        menu_action.print_menu()
        menu_action.get_user_input()

        if menu_action.users_item_choice is None:
            print("\nSorry! >>> Wrong choice <<<")
            time.sleep(1)
            continue

        if menu_action.get_menu_item_number() == 1:
            ask_for_input(atm, menu_action, "Enter amount to deposit: ")
            print(f"Balance: {atm.get_balance()}")

        elif menu_action.get_menu_item_number() == 2:
            ask_for_input(atm, menu_action, "Enter amount to withdraw: ")
            print(f"Balance: {atm.get_balance()}")

        elif menu_action.get_menu_item_number() == 3:
            print(f"The balance is {atm.get_balance()}")

        elif menu_action.get_menu_item_number() == 4:
            print(f"\n{menu_action.users_item_choice[1]}")
            print(f"The balance is {atm.get_balance()}")
            time.sleep(1)
            ask_for_input(atm, menu_action, None)

        elif menu_action.get_menu_item_number() == 5:
            print("\nLog book records:", end="")
            atm.print_log()

        elif menu_action.get_menu_item_number() == 6:
            print("Exit the program...")
            continue_to_run = False

            exit(0)

        input("Press ENTER to continue")


if __name__ == '__main__':
    main()
