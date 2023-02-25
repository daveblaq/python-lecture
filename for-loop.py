# Used for iterating over a sequence
mydict = ['ji', 'ju', 'jo']

for values in mydict:
			print(values)
			if values == 'ju':
							break


for x in range (3, 7):
				print(x)

for x in range(7):
			print(x)
else: 
			print('Finished Looping!!')

my_list = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

print(my_list[0][0])

# Nested Loop (having a for loop in a for loop)
for lists in my_list:
			for row in lists:
				print(row)
