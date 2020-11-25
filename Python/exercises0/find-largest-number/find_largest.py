# the `numbers` argument for this function will always be a list.
def find_largest(numbers):
    max_num = 0
    for num in numbers:
        if max_num < num:
            max_num = num

    return max_num


some_numbers = [55, 34, 100, 32, 0, 88, 9]

largest = find_largest(some_numbers)

print(largest)
# the expected output here is: `100`
