# Strings
# text and characters
# Syntax
# " " and ' '


# Define a string
my_string = 'Hey I am a cool string B)'
print(my_string)

# check its type
print(type(my_string))

# Concatenation
# adding of two strings
joint_string = my_string + 'This is another string'
print(joint_string)

# example 2 of concatenation
name = 'Mohamed'
welcome_text = 'WELCOME TO SPARTAAAAAAA (300)'
print(welcome_text + ' ' + name)
print(welcome_text, name) #overloading the print method

# Interpolation
# inserting a string inside another string
# or running python inside a string
print(f'WELCOME {name} TO CLASS 54, we are Contested Terrain')

# useful methods
# belong to specific data types
example_long_str = '     HELLO, THIS is a veRY BAdly formated text?    '
print(example_long_str)

# remove trailing white space
print(example_long_str.strip())

#lower case
print(example_long_str.lower())

# upper case
print(example_long_str.upper())


# capitalize first character
print(example_long_str.capitalize())


# capitalize first character fo each word
print(example_long_str.title())


# change ? into !
print(example_long_str.replace('?','!'))

# chain methods to remove white space & make presentable
print((example_long_str.strip()).capitalize())

# Create list with individual words
print(example_long_str.split())