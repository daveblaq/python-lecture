# A block of code which performs a particular task
def greetings_function(name, age):
	print('Welcome '+ name + '. You are '+ str(age)+ ' years old.')

	
greetings_function('David', 27)

# Passing many arguements/params
def greetings_function(*names):
	print('Welcome ' + names[1])


greetings_function('David','Tom', 'Jerry')
