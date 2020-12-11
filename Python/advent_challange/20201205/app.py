'''
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass!
You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that
suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input);
perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified
like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
(numbered 0 through 127). Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or
the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until
you're left with exactly one line.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep
the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example,
the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

Your puzzle answer was 801.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However,
there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

answer= 597

'''
import math

raw_file = open("input.txt").readlines()

boardingpass_list = []
new_boarding_list = []

for num in range(len(raw_file)):
    line = raw_file[num].strip()

    boardingpass_list.append(line)


def divide(num_list, fbrl):
    z = num_list[1] - num_list[0]
    x = math.ceil(z / 2)

    if fbrl in ['F', 'L']:
        return [num_list[0], num_list[1] - x]
    else:
        return [num_list[0] + x, num_list[1]]


def calc_row_seat(passport_code, row_num_range, seat_num_range):
    row = []
    seat = []

    for char in passport_code:
        if char in ['F', 'B']:
            row = divide(row_num_range, char)
            row_num_range = row
        elif char in ['R', 'L']:
            seat = divide(seat_num_range, char)
            seat_num_range = seat

    return [row[0], seat[0], row[0] * 8 + seat[0]]


def part1():
    seat_id = 0

    for bpass in boardingpass_list:
        row_num_range = [0, 127]
        seat_num_range = [0, 7]

        res = calc_row_seat(bpass, row_num_range, seat_num_range)

        new_boarding_list.append([bpass, res[0], res[1], res[2]])
        seat_id = res[2] if res[2] > seat_id else seat_id

    print(seat_id)


def part2():
    part1()
    x = []
    for seat in new_boarding_list:
        print(seat)
        x.append(seat[3])
    x.sort()

    cnt = 0
    for s in x:
        try:
            if s + 1 != x[cnt + 1]:
                print(x[cnt], x[cnt + 1])
            cnt += 1
        except:
            pass

part2()