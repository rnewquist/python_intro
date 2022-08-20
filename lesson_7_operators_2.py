# Mostly everyone knows basic math operators
2+2  # 4
2-1  # 1
2*3  # 6
2/2  # 1.0 notice how division always returns a float

# However in programing, there are more operators that we can use to perform math
# Power mulitplication 2^3:
2**3  # 12
pow(2, 3)  # 12

# The '%' means modulus operator
# This operator is similiar to division, but returns the remainder
print("---\n")
print(14/6)  # 2.33333
# Performing the math on this, we can see that 6 goes into 14 two times
# Leaving a remainder of 2/6 (14-12 = 2)
# Performing a modulus operator will then return a 2
print("---\n")
print(14 % 6)
# In the case of taking a modulus of 6, the return is always going to be between 0-5
# When the number has no remainder, it returns 0
print(6 % 6)  # 0
print(5 % 6)  # 5

# Sometimes we dont care about the remainder and just want to know how many whole times a number goes into another
# For this we use '//' floor division
# Floor just means that if there is a decimal, we always round down, 3.9 -> 3
print("---\n")
print(14//6)  # 2
# Floor division will always return an int and is the opposite of '%'

# We often want to compare numbers too
# min() is used to find the smallest number
min(3, 5)  # 3
# min() can also take in a list of numbers
min([6, 5, 4, 7, 6, 3, 1]) # 1
# max is the same thing but returns the highest number
min(3, 5)  # 5
min([6, 5, 4, 7, 6, 3, 1]) # 7

# Other two math operators worth noting are:
# round()
round(3.45) # 3
round(3.5) # 4

# abs() absolute value
abs(1) # 1
abs(-1) # 1

# --- Practice ----
# Create a for loop from range 1 to 100
# Print the numbers that are a multiple of 12
# Count how many multiples of 12 there are
# At the end of the for loop, print the total amount of numbers that are a multiple of 12
# Hint: use '%'