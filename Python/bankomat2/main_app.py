import time
import repo.bankomat
import repo.helpers
import repo.menus

actions = [
    (0, "Dummy", "Dummy"),
    (1, "Deposit money", "deposit"),
    (2, "Withdraw money", "withdraw"),
    (3, "Check balance", "get_balance"),
    (4, "Collect interest", "collect_interest"),
    (5, "Print log", "print_log"),
    (6, "End program", "end"),
]


def menu_start():
    print("Welcome to the bank of Zeros and Ones")


def get_pin_code():
    try:
        input_pin = int(input("Enter your pin, 4 or 6 digits: "))
    except:
        input("ERROR: Invalid pin! Press ENTER to continue.")
        return -1

    return input_pin


def cash_machine_setup():
    global bankomat
    bankomat = repo.bankomat.Cash_machine(2345, 10921)


def prepare_menus():
    global menu_action
    menu_action = repo.menus.Menu(actions)


def main():
    repo.helpers.clear()
    menu_start()
    cash_machine_setup()
    prepare_menus()

    bankomat.get_pin()

    continue_to_run = True

    while continue_to_run:
        repo.helpers.clear()
        menu_action.print_menu()
        menu_action.get_user_input()

        if menu_action.users_choice == -1:
            print("Sorry! Wrong choice.")
            time.sleep(1)
            continue

        if menu_action.users_choice == 1:
            amount = input("Enter amount to deposit: ")
            bankomat.call_function(menu_action.get_function_to_run(), amount)
        elif menu_action.users_choice == 2:
            amount = input("Enter amount to withdraw: ")
            bankomat.call_function(menu_action.get_function_to_run(), amount)
        elif menu_action.users_choice == 3:
            print(bankomat.call_function(menu_action.get_function_to_run(), amount))
            input("Press ENTER to continue")
        elif menu_action.users_choice == 4:
            bankomat.call_function(menu_action.get_function_to_run(), amount)
        elif menu_action.users_choice == 5:
            bankomat.call_function(menu_action.get_function_to_run(), amount)
            input("Press ENTER to continue")
        elif menu_action.users_choice == 6:
            print("Exit the program...")
            continue_to_run = False

    exit(0)


if __name__ == '__main__':
    main()
