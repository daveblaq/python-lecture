from copyreg import constructor


countries = ["United kingdom", "Ghana", "Nigeria", "Australia", "New Zealand"]

# Getting value from their index number in python
print(countries[0])

# Printing from a particular point from a list
print(countries[1:4])

# Get the type of a particular variable
print(type(countries))

# Change the an item in a list 
countries[0] = 'United States'
print(countries)

# getting list items from the last value all to the first value (use negative sign and number to specify the point to print from)
print(countries[-1])

# Get Total number of items in a list
print(len(countries))

# Get Type of item in a list
print(type(countries[0]))

# Using the list constructor to construct a list
fruits = list(('Apple', 'Orange', 'Banana', 'Avocado'))
print(fruits)

