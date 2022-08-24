# Loops are while you want to run code repeatedly
# For instance if I want to print "Hi" 6 times
# The code will be:
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

# However, that makes the code complex very fast
# Loops allow code to be repeated as many times as we designate
# The while loop takes in a boolean: while(boolean)
# if that boolean is true, the code will run below it
# then the code will check if the boolean is true again
int_var = 0
while(int_var < 5):
    int_var = int_var + 1 # This will increment int_var by 1 every time the while loop is ran
    print(int_var)
# 1
# 2
# 3
# 4
# 5

# int_var starts at 0, the operator for the while loop is True
# because it is less that 5
# int_var increases by 1 every time the while loop runs
# once the code below the while loop is ran
# the while loop gets checked again to see if it needs to run again
# This is why int_var stops getting incremented at 5 because 5 isn't less than 5

# Now if we can use this logic to print "Hi" as many times as we want
int_var = 0
while(int_var < 5):
    int_var = int_var + 1
    print("Hi")

# By changing 5 to what ever we want, we can print "Hi" as many times as we want
# We can also change the 5 to a variable to read the code more easily
int_var = 0
print_amount = 5
while(int_var < print_amount):
    int_var = int_var + 1
    print("Hi")

# Note that if the boolean in the while loop is never false
# The code will never stop running

# ----- Practice -----
# Create a while loop that will count down from 5
# Print every int during the loop
