import time
import repo.bankomat
import repo.helpers
import repo.menus

number_of_pin_tries = 3
valid_pin_length = [4, 6]
pin_code_for_testing = '2345'
balance_for_testing = 10324
atm = None
menu_action = None

main_menu_repo = [
    (0, "Dummy", "Dummy"),
    (1, "Deposit money", "deposit"),
    (2, "Withdraw money", "withdraw"),
    (3, "Check balance", "get_balance"),
    (4, "Collect interest", "collect_interest"),
    (5, "Print log", "print_log"),
    (6, "End program", "end"),
]


def get_pin():
    global number_of_pin_tries

    while number_of_pin_tries > 0:
        # pin = input("Enter your pin, 4 or 6 digits: ")
        pin = input("Enter your pin, 4 or 6 digits: ") or pin_code_for_testing  # FOR TESTING ONLY

        if validate_pin(pin):
            return True

        number_of_pin_tries -= 1
        print(f"ERROR: Invalid pin! {number_of_pin_tries} tries left")

    return False


def validate_pin(pin):
    is_valid = False

    if not pin.isdigit():
        is_valid = False
    elif len(pin) not in valid_pin_length:
        is_valid = False
    elif atm.pin == int(pin):
        is_valid = True

    return is_valid


def cash_machine_setup():
    return repo.bankomat.atm(int(pin_code_for_testing), balance_for_testing)


def prepare_menus():
    return repo.menus.Menu(main_menu_repo)


def main():
    global atm, menu_action
    atm = cash_machine_setup()
    menu_action = prepare_menus()

    repo.helpers.clear()
    print("Welcome to the bank of Zeros and Ones")

    if not get_pin():
        print("ERROR: No valid pin")
        print("Exit the program...")
        exit(1)

    continue_to_run = True
    while continue_to_run:
        repo.helpers.clear()
        menu_action.print_menu()
        menu_action.get_user_input()

        if menu_action.users_item_choice is None:
            print("Sorry! Wrong choice.")
            time.sleep(1)
            continue

        if menu_action.get_menu_item_number() == 1:
            amount = input("Enter amount to deposit: ")
            atm.call_function(menu_action.get_function_to_run(), amount)
        elif menu_action.get_menu_item_number() == 2:
            amount = input("Enter amount to withdraw: ")
            atm.call_function(menu_action.get_function_to_run(), amount)
        elif menu_action.get_menu_item_number() == 3:
            print(atm.call_function(menu_action.get_function_to_run(), 0))
            input("Press ENTER to continue")
        elif menu_action.get_menu_item_number() == 4:
            atm.call_function(menu_action.get_function_to_run(), 0)
        elif menu_action.get_menu_item_number() == 5:
            atm.call_function(menu_action.get_function_to_run(), 0)
            input("Press ENTER to continue")
        elif menu_action.get_menu_item_number() == 6:
            print("Exit the program...")
            continue_to_run = False

    exit(0)


if __name__ == '__main__':
    main()
