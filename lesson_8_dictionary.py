exampleList = [1,2,3,4,5]
firstVariable = exampleList[0]
lastVariable = exampleList[-1]
searchIndex = 0
exampleList[searchIndex]

dictionary = {}
dictionary = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5
}
dictionary[0] == exampleList[0]
dictionary[4] == exampleList[4]

dictionary = {
    "one": "first",
    "two": "second",
    "three": "third"
}
dictionary["one"] == "first"

for key in dictionary:
    print(key)

print(dictionary.keys())

print(dictionary.values())

complexDictionary =  {
    "this is a key": "this is a value",
    "this value can be almost anything": dictionary
}

print(complexDictionary.keys())
print(complexDictionary.values())

for key in dictionary:
    dictionary[key]

# ----- Example -----
list1 = [1,2,3,4,5]
list2 = ["a","b","c"]
list3 = [True, True, False, True]
# Create a dictionary of the three lists above, make the keys
# ints, bools, and strings
# Then go through that dictionary and print out they value
# of the lists and what key it belongs to, e.g. int - 1, bool - Flase
