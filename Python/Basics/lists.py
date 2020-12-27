'''
Python Lists

The list is a most versatile datatype available in Python which can be written as a list of comma-separated
values (items) between square brackets. Important thing about a list is that items in a list need
not be of the same type.

Creating a list is as simple as putting different comma-separated values between square brackets.
For example −
'''

# Creating a List
List = []
print("Blank List: ")  # Blank List:
print(List)            # []


# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")  # List of numbers:
print(List)                   # [10, 20, 14]

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")  # List Items:
print(List[0])           # Geeks
print(List[2])           # Geeks

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")  # Multi-Dimensional List:
print(List)                          # [['Geeks', 'For'], ['Geeks']]

'''
Creating a list with multiple distinct or duplicate elements

A list may contain duplicate values with their distinct positions and hence,
multiple distinct or duplicate values can be passed as a sequence at
the time of list creation.
'''

# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")  # List with the use of Numbers:
print(List)                                # [1, 2, 4, 4, 3, 3, 3, 6, 5]

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")  # List with the use of Mixed Values:
print(List)                                     # [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# Knowing the size of List
# Creating a List
List1 = []
print(len(List1))  # 0

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))  # 3

'''
Adding Elements to a List
Using append() method

Elements can be added to the List by using built-in append() function.
Only one element at a time can be added to the list by using append() method, for addition
of multiple elements with the append() method, loops are used. Tuples can also be added to the
List with the use of append method because tuples are immutable. Unlike Sets, Lists can also be
added to the existing list with the use of append() method.
'''
# Creating a List
List = []
print("Initial blank List: ")  # Initial blank List:
print(List)                    # []

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")  # List after Addition of Three elements:
print(List)                                         # [1, 2, 4]

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")  # List after Addition of elements from 1-3:
print(List)                                            # [1, 2, 4, 1, 2, 3]

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")  # List after Addition of a Tuple:
print(List)                                  # [1, 2, 4, 1, 2, 3, (5, 6)]

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")  # List after Addition of a List:
print(List)                                 # [1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]

'''
Using insert() method

append() method only works for addition of elements at the end of the List, for addition of
element at the desired position, insert() method is used. Unlike append() which takes only one argument,
insert() method requires two arguments(position, value).
'''
# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")  # Initial List:
print(List)              # [1, 2, 3, 4]

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")  # List after performing Insert Operation:
print(List)                                          # ['Geeks', 1, 2, 3, 12, 4]

'''
Using extend() method

Other than append() and insert() methods, there’s one more method for Addition of elements, extend(),
this method is used to add multiple elements at the same time at the end of the list.

Note – append() and extend() methods can only add elements at the end.
'''
# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")  # Initial List:
print(List)              # [1, 2, 3, 4]

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")  # List after performing Extend Operation:
print(List)                                          # [1, 2, 3, 4, 8, 'Geeks', 'Always']


