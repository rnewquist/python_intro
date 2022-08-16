# Variables only hold one value, x = 1
# Lists hold as many variables as you'd like
list_var = list()
list_var = []

# Lists are a variable that holds multiple varibles inside of it
string_list = ['first', 'second', 'third']
int_list = [1, 2, 3]

# Lists are created by using [] and using a comma to separate each value
# Common rule is that a list should hold only the same type of variables
# Though lists can hold multiple types of variables
multi_list = [1, 'one', 1.0, False]

# A list can even hold a list inside of itself creating a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8 , 9]]

# once a list is created you can access any index of the list
# the first variable in a list is initialized at 0

print(string_list[0])
# first

# These index have to be numbers, but that number can be represented by a variable
first_index = 0
second_index = 1
print(string_list[first_index])
print(string_list[second_index])
# first
# second

# Accessing a variable in a list that doesn't exist will result in an error and the program crashing
# string_list[4] would result in a crash
# this is solved by finding the size of the list using len()
print(len(string_list))
# 3
print(len(list()))
# 0

# ----- Practice -----
# using string_list, use a while loop to print each item in the list one at a time
# make sure to stop the while loop to not access an index that doesn't exist
string_list = ['first', 'second', 'third', 'fourth']


