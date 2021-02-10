import string
import sys
from functools import reduce

bibletxt = str(''.join(list(filter(lambda x: x in string.ascii_letters or x == ' ', open('bible.txt').read())))).split(' ')
L = len(bibletxt)
biblehashlen = 16


def biblehash(x):
    noise = [
        432, 130, 349, 554,
        395, 293, 146, 947,
        492, 958, 111, 879,
        410, 000, 666, 959,
        795, 485, 132, 269,
        L,   int(L/2), int(L/3), int(L/4),
        0,   1,   2,   3
    ]

    shifts = reduce(lambda a, b: dict(a, **b), map(lambda item: {item[1]: item[0]}, enumerate(x)))

    return reduce(
        lambda a, b: ((a + '_') if isinstance(a, str) else '') + bibletxt[b[1] % (len(bibletxt) - 1)],
        map(
            lambda i: (
                x[i % (len(x) - 1)],
                ord(x[i % (len(x) - 1)]) + shifts[x[i % (len(x) - 1)]] + reduce(
                    lambda a, b: a + b,
                    [noise[(ord(c) + i) % (len(noise) - 1)] for c in x]
                )
            ),
            range(biblehashlen)
        )
    )

print(biblehash(sys.argv[1]))
