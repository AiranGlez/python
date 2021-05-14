myList = ['Glock', 'Beretta', 'M4', 'AK-47']

print(myList[0])

print(myList[1:2])

print(myList[2:])

# Aggregate elements to list

myList.append('Flamethrower')

print(myList[:])

# Aggregate element to specific position on the list

myList.insert(2, 'L-96')

print(myList[:])

# Aggregate multiple elements to list

myList.extend(['RPG', 'Magnum 44.'])

print(myList[:])

# Return element index

print(myList.index('M4'))

# Check if element is on list

print('AK-47' in myList)

print('AK-74' in myList)

# Remove element

myList.remove('Flamethrower')

print(myList[:])

# Remove last element

myList.pop()

print(myList[:])

# Concatenate lists

myList2 = ['SPAS-12', 'Hunting Rifle']

myList3 = myList + myList2

print(myList3[:])