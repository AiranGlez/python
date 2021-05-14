myTuple = ('One', 'Two', 'Three', 'Four')

print(myTuple[2])

# Create a list from a tuple

myList = list(myTuple)

print(myList)

# Count how many elements are in the list

print(myTuple.count('Two'))

# Check tuple length

print(len(myTuple))

# Unitary tuple

unitaryTuple = ('Unitary',)

# Tuple packing

myTuple2 = 'Charles', 1, 11, 1983

name, day, month, year = myTuple2

print(name, day, month, year)
