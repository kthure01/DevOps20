import math

char_list = ['0', 'i', ' ']
rows = 10
width = rows + (rows - 1)


def swap_char():
    char_list[0], char_list[1], char_list[2] = char_list[1], char_list[0], char_list[2]


def swap_start_char(row_number):
    if row_number % 2 != 0:
        swap_char()


def triangle(print_number_of_rows):
    width = print_number_of_rows + (print_number_of_rows - 1)
    for x in range(1, print_number_of_rows + 1):
        row = ''
        swap_start_char(x)
        for y in range(x + (x - 1)):
            if y % 2 == 0:
                row += char_list[0]
                swap_char()
            else:
                row += char_list[2]

        print(f"{row:^{width}}")


def tri_force(print_number_of_rows):
    row_width = print_number_of_rows + (print_number_of_rows - 1)
    row_to_be_blank = math.floor(print_number_of_rows / 2) + 1

    n = 1
    for row_number in range(1, print_number_of_rows + 1):
        row_to_print = ''
        swap_start_char(row_number)

        if row_number < row_to_be_blank:
            row_to_print = upper_tri(row_number)
        elif row_number > row_to_be_blank:
            row_to_print = lower_tri(n, row_number)
            n += 1

        print("{0:^{1}}".format(row_to_print, row_width))


def lower_tri(row_no_lower, row_no):
    row = ''
    pos_to_blank = row_no_lower + (row_no_lower - 1)

    first_pos = pos_to_blank + 1
    last_pos = row_no + (row_no - 1) - pos_to_blank - 2
    for pos_in_row in range(row_no + (row_no - 1)):
        if pos_in_row % 2 == 0 and pos_in_row not in [first_pos, last_pos]:
            row += char_list[0]
            swap_char()
        else:
            row += char_list[2]

    return row


def upper_tri(row_number):
    row_to_print = ''
    for y in range(row_number + (row_number - 1)):
        if y % 2 == 0:
            row_to_print += char_list[0]
            swap_char()
        else:
            row_to_print += char_list[2]

    return row_to_print


def multiplication(number):
    lista = []
    tmp_str = ''
    for row in range(1, number + 1):
        for item in range(1, number + 1):
            tmp_str += "{} ".format(str(row * item))

        lista.append([tmp_str])
        tmp_str = ''

    # for row in lista:
    #     print(*row, sep=" ")

    row_format = "{:<2}" * (len(lista) + 1)
    print(row_format.format(*lista))
    # for team, row in zip(lista, data):
    #     print(row_format.format(team, *row))


def main():
    print("1) Skriv ut en triangel")
    print("2) Skriv ut en tri-force")
    print("3) Skriv ut en plutifikationstabell")
    str = input("Välj: ")

    if '1' in str:
        triangle(int(input("Ange antal rader att skriva ut: : ")))
    elif '2' in str:
        tri_force(int(input("Ange antal rader att skriva ut: : ")))
    elif '3' in str:
        pass
    else:
        exit()


if __name__ == '__main__':
    multiplication(10)
    # main()
