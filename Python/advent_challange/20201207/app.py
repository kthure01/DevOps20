'''
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to
grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents;
bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible
for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty,
every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors
would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny
gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your
    shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure
you get all of it.)

Your puzzle answer was 164.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
answer = 7872
'''

raw_file = open("input.txt").readlines()

list_of_colours = {}
cnt = 0
for num in range(len(raw_file)):
    line = raw_file[num].strip()

    if len(line) > 0:
        x, y = line.split(' bags contain ')
        '''
            Line 148: dotted lavender bags contain 5 wavy cyan bags, 2 dark indigo bags, 4 shiny gold bags.
            Line 197: drab white bags contain 4 shiny tomato bags, 3 shiny gold bags, 3 dull lime bags, 3 plaid orange bags.
            Line 342: muted gold bags contain 2 wavy gray bags, 4 clear gold bags, 1 shiny gold bag.
            Line 474: shiny gold bags contain 5 bright maroon bags, 5 shiny aqua bags, 2 clear lime bags, 2 muted white bags.
            Line 497: striped beige bags contain 1 clear gold bag, 1 vibrant white bag, 3 faded cyan bags, 2 shiny gold bags.
            Line 536: vibrant coral bags contain 3 wavy lime bags, 2 shiny gold bags, 1 dotted orange bag, 3 muted indigo bags.
        '''
        if 'dotted lavender' in line or 'drab white' in line or 'muted gold' in line or 'vibrant coral' in line or 'striped beige' in line:
            cnt += 1
            # tmp.append(f1.strip(',').strip())
            print(x, y)
            # continue

        # rx = '( bags)|( bag)'
        # k1 = re.split(rx, y)
        # tmp = []
        # for f1 in k1:
        #     if f1 is None or len(f1) < 6 or 'other' in f1: continue
        #     splitted = f1.split(' ')
        #     if ' white' in splitted[2] or ' yellow' in splitted[2] or ' orange' in splitted[2] or ' red' in splitted[2]:
        #         cnt += 1
        #         tmp.append(f1.strip(',').strip())
        #         print(x, tmp)
        #
        # list_of_colours[x] = tmp

    # if len(line) == 0 or num == len(raw_file) - 1:
    #     list_of_colours .append(tmp.copy())
    #     tmp.clear()

print("Answers is: " + str(cnt))
