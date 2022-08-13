# There are times when you want to run certain code based on conditions
# The simpliest way to do this is use if else statments
# These statements take boolean values and run them based on true or false

if(True):
    print("This code will run")
else:
    print("This code will not run")

# Because the boolean in the if section is True, that code will run
# The code in the else statement will never run while the boolean is True in
# When writing the if/else statement, the boolean will be surrounded by ()
# After the () there will be a :
# The lines below will have an indent
# This indent will be for all code you want to run based on the condition

# Set bool_var to True/False to see the different results
bool_var = False
if(bool_var):
    print("bool_var is set to True")
else:
    print("bool_var is set to False")
print("This line is not in the if/else statement")