def generatePairs(limit):

    num = 1

    myList = []

    while num < limit:

        myList.append(num * 2)

        num = num + 1

    return myList

print(generatePairs(10))

# Using a generator

def generatePairs(limit):

    num = 1

    while num < limit:

        yield num * 2

        num = num + 1


getPairs = generatePairs(10)

#for i in getPairs:
#    print(i)

# One by one

print(next(getPairs))

print(next(getPairs))

# Using yield from

# '*' indicates that this function will receive an indeterminate number of parameters in tuple form


def generate_cities(*cities):
    for element in cities:
        yield from element


returned_cities = generate_cities('Madrid', 'London', 'Bilbao', 'Manchester')

print(next(returned_cities))

print(next(returned_cities))

