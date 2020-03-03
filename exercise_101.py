# practice string
# Welcome to Sparta - exercise

# Version 1 specs
# define a variable name, and assign a string with a name
name = 'Kevin Monteiro'

# prompt the user for input and ask the user for his/her name

# use concatenation to print a welcome message and use method to format the name/input

# Version 2 - with interpolation
# Do the same but use a different message

# ask the user for a first name, save it in a variable
first_name = (input("What is your first name?")).strip().Capitalize()

# ask the user for a last name, save it in a variable
last_name = (input("What is your last name?")).strip().capitalize()

# use interpolation to print the message
print(f'Welcome {first_name} {last_name}!')

#Calculate year of birth
age = int(input("How old are you?"))
year_of_birth = 2020-age
print(f'OMG {first_name} {last_name}, you are {age} years old so you were born in {year_of_birth}')
