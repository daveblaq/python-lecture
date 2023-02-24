list1 = [4, 3, 5, 1, 2]
list2 = ['banana', 'apples', 'mango', 'oranges']


# Add / Extend two lists together
list1.extend(list2)
print(list1)

# Add a value to a list
list2.append('cherry')
print(list2)

# Fix a value in a particular position of a lit (takes the index number and the value)
list2.insert(1, 'cherry')
print(list2)

# Remove a value from a list
list2.remove("banana")
print(list2)

# Get the index value of a item in a list
print(list2.index('mango'))

# Check number of times a value appears in a list
print(list2.count('mango'))

# Print a scattered list of integers in accending order
list1.sort()
print(list1)

# Delete a value from a list
del list2[0]
print(list2)

# Print a list in descending order
list2.reverse()
print(list2)

# Duplicate a list 
list3 = list2.copy()
print(list3)

# Remove the last value of a list (you can also remove from position using the index value)
list2.pop()
print(list2)

# Clear everything in a list
list2.clear()
# or
del list2
print(list2)

