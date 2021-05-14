myDictionary = {
    'Spain': 'Madrid',
    'Germany': 'Berlin',
    'France': 'Paris',
    'United Kingdom': 'London'
}

print(myDictionary['France'])

# Aggregate elements to dictionary

myDictionary['Italy'] = 'Lisbon'

# Modify value of element

myDictionary['Italy'] = 'Rome'

print(myDictionary)

# Remove element

del myDictionary['Italy']

print(myDictionary)

# Dictionary with different value types

myDictionary2 = {
    'id': 2,
    15: 'user',
    True: 'thisistrue'
}

print(myDictionary2)

# Return dictionary keys

print(myDictionary.keys())

# Return dictionary values

print(myDictionary.values())

# Return dictionary length

print(len(myDictionary))