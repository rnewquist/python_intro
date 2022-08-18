# A while loop will run until you tell it to stop
# If we want a loop that will run through a list we do the following
start = 0
items = [1, 2, 3, 4, 5, 6]
while (start < len(items)):
    print(items[start])
    start = start + 1
# This requires us to set an integer to start the loop
# It requires us to increment that integer
# And it require us to use item[start] to get variable at the index start
# There is an easier way, using a for loop
print("---\n")
for item in items:
    print(item)
# This will go through the entire list given to it
# and return the variable one at a time with the name 'item'
# for the_indexed_variable in the_list_of_variables

# We are not required to start with a list though
# We can use the range() function to create a range of numbers
# Note that the range value with be one less that the selected number since it starts at 0
# range(end)

print("---\n")
for item in range(7):
    print(item)

# We can also start at another number than 0
# By entering two number in range(), we can set the starting number
# range(start, end)

print("---\n")
for item in range(4, 7):
    print(item)

# Finally we can add a third number to range() if we want to increase it by more than one per loop
# See what happens when we start the range at 0, end at 5, and step by 2

print("---\n")
for item in range(0, 7, 2):
    print(item)

# The value of items increases by two every loop instead of one
# range(start, end, step)

# --- Practice ----
# Create a for loop that will only print out multiples of 7, e.g. 0, 7, 14
# Make the loop go to 70 variables
