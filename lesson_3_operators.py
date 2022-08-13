# Bool values are how you use if else statements
# Operators allow you to turn variables into booleans
# '==' operator checks if the left of the operator is equal to the right
1 == 1 # True
1 == 0 # False
"String" == "String" # True
"String" == "Strong" # False

# '!=' operator will check if the left of the operator is different to the right
1 != 1 # False
1 != 0 # True
"String" != "String" # False
"String" != "Strong" # True

# You can set the result of this operator to a variable too
bool_var = 1 == 1
print(bool_var)
# True

# You can compare any type of variable to another
"String" == 1 # False
"1" == 1 # False

# With floats and ints, they can be compared
1.0 == 1 # True
1.1 == 1 # False

# Other operators are only to deal with numbers
# '>' checking if the left of the operator is greater the right
1 > 0 # True
0 > 1 # False
1 > 1 # False because 1 is not greater than 1 but equal

# '>=' checks if the left of the operator is greater or equal to the right
1 >= 0 # True
0 >= 1 # False
1 >= 1 # True

# '<' checking if the left of the operator is less the right
1 < 0 # False
0 < 1 # True
1 < 1 # False because 1 is not greater than 1 but equal

# '<=' checks if the left of the operator is less or equal to the right
1 <= 0 # False
0 <= 1 # True
1 <= 1 # True

