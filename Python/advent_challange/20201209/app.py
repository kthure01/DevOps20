'''
--- Day 9: Encoding Error ---

With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little
screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several
paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you,
is an old cypher with an important weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any
two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more
than one such pair.

For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid,
the next number must be the sum of two of those numbers:

    26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
    49 would be a valid next number, as it is the sum of 24 and 25.
    100 would not be valid; no two of the previous 25 numbers sum to 100.
    50 would also not be valid; although 25 appears in the previous 25 numbers, the two numbers in the pair
    must be different.

Suppose the 26th number is 45, and the first number (no longer an option, as it is more than 25 numbers ago) was 20.
Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to it:

    26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
    65 would not be valid, as no two of the available numbers sum to it.
    64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.

Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers;
the only number that does not follow this rule is 127.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

Your puzzle answer was 1309761972.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a
contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127.
(Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range;
in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
answer = 177989832
'''

xmas = {}
for row, num in enumerate(open("input.txt").read().strip().split('\n')):
    xmas[row + 1] = int(num)


def check1(num_dict, num_to_check):
    result = [False, 0, 0]
    for key1 in num_dict.keys():
        for key2 in num_dict.keys():
            if key1 == key2:
                continue

            result[1] = num_dict[key1]
            result[2] = num_dict[key2]

            if num_dict[key1] + num_dict[key2] == num_to_check:
                result[0] = True

    return result


def part1():
    start_x = 1
    stop_y = 25
    step_cnt = 1
    num_to_check = 0
    res = {}

    while True:
        res.clear()
        res = {key: val for key, val in filter(lambda sub: start_x <= int(sub[0]) <= stop_y, xmas.items())}
        num_to_check = xmas[stop_y + 1]

        res1 = check1(res, num_to_check)
        if res1[0]:
            start_x += step_cnt
            stop_y += step_cnt
        else:
            print('fail', start_x, stop_y, num_to_check, res1)
            break


part1()


def check2(num_dict, num_to_check):
    result = [False, '']
    num_sum = 0
    lista = []
    for cnt, key1 in enumerate(num_dict.keys(), start=1):
        lista.append(num_dict[key1])
        num_sum += num_dict[key1]

        if num_sum == num_to_check and cnt > 1:
            lista.sort()
            result = [True, lista]

    return result


def part2():
    num_to_find_in_part2 = 1309761972
    start_x = 510
    stop_y = 511
    step_cnt = 1
    res = {}

    loop = 0
    while True:
        loop += 1
        res.clear()
        res = {key: val for key, val in filter(lambda sub: start_x <= int(sub[0]) <= stop_y, xmas.items())}

        res1 = check2(res, num_to_find_in_part2)
        if not res1[0]:
            stop_y += step_cnt
            if stop_y - start_x == 20:
                step_cnt = 1
                start_x += step_cnt
                stop_y = start_x + 1
        else:
            print('true', loop, start_x, stop_y, num_to_find_in_part2, res1)
            print('sum', res1[1][len(res1[1]) - 1] + res1[1][0])
            break


part2()
