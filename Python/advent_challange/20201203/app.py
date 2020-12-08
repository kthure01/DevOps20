'''
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy,
it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which
angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and
biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom
(below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square
and X where there was a tree:
1234
0123
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

Your puzzle answer was 237.

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the
top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together,
these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

answer = 2106818610

'''

raw_data_file = open('input.txt').readlines()

data_list = []
for line in raw_data_file:
    data_list.append(line.rstrip())


def part1():
    x_direction_cnt = 3
    row_cnt = 0
    str_repeat_times = 1
    tree_cnt = 0

    for line in data_list:
        row_cnt += 1

        # var 10'e rad förlänger vi strängen
        if row_cnt % 10 == 0:
            str_repeat_times += 1

        work_str_as_list = list('{}'.format(line * str_repeat_times))

        if row_cnt == 1:
            continue

        if work_str_as_list[x_direction_cnt] == '#':
            tree_cnt += 1
            work_str_as_list[x_direction_cnt] = 'X'
        else:
            work_str_as_list[x_direction_cnt] = '0'

        x_direction_cnt += 3

        # print(f'{row_cnt}: {line}')
        print(f'{row_cnt}: {x_direction_cnt} | {tree_cnt} | {"".join(work_str_as_list)}')


def part3(x_move, y_move):
    x_move_cnt = 0
    tree_cnt = 0
    str_repeat_times = 0

    for num in range(0, data_list.__len__(), y_move):

        if num % int(len(data_list[num]) / x_move) == 0:
            str_repeat_times += 1

        if num == 0:
            x_move_cnt += x_move
            continue

        work_str_as_list = list('{}'.format(data_list[num] * str_repeat_times))

        if work_str_as_list[x_move_cnt] == '#':
            tree_cnt += 1
            work_str_as_list[x_move_cnt] = 'X'

        x_move_cnt += x_move
        print(num, tree_cnt, work_str_as_list)

    return tree_cnt


run_list = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]
prod = 1
for x, y in run_list:
    sum = part3(x, y)
    prod *= sum
    print(x, y, sum, prod)

# prod = part3(3, 1)

print(prod)
# too low 1441507470
