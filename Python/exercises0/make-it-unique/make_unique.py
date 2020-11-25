def make_unique(names):
    return set(names)


my_names = ["John", "Sarah", "Hannah", "Hannah", "Tom", "George", "Sarah"]

unique_names = make_unique(my_names)

print(unique_names)
# The correct answer here should be:
#   `['Sarah', 'Hannah', 'John', 'George', 'Tom']`
