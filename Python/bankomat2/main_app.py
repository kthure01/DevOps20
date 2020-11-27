import repo.bankomat
import repo.helper
import repo.menus

actions = [
    "Deposit money",
    "Withdraw money",
    "Check balance",
    "Collect interest",
    "End program",
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


def main():
    bankomat = repo.bankomat.Cash_machine(2345, 10921)
    repo.helper.clear()
    menu_action = repo.menus.Menu(actions)

    menu_start()

    if not bankomat.get_pin():
        print("Sorry! Exiting the program!!!")
        exit(-1)

    repo.helper.clear()
    menu_action.print_menu()
    menu_action.get_user_input()

    # main()
    # input("VÄNTA")


if __name__ == '__main__':
    main()
