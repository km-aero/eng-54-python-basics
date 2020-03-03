# Define the following variables
# name, last_name, species, eye_color, hair_color, age
name = 'Lana'

# Prompt user for input and Re-assign these
name = input('what new name would you like?\n')
last_name = input('New last name?\n')
species = input('species?\n')
eye_colour = input('eye colour?\n')
hair_colour = input('hair colour?\n')
age = int(input('age?\n'))

## Calculate year of birth
# import time
# calculate the difference

from datetime import date as dt

today = dt.today().year
year_of_birth = today - age

print(f'Hello {name} {last_name}! Welcome, your age is {age}, your year of birth is {year_of_birth},\n'
      + f'your eyes are {eye_colour} and your hair color is {hair_colour}.')

# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'


# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age




# calculate the difference and year of birth for each
# print out these formatted. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>.
# This is <difference_y> later than <mom_name> who was on on <y_birth_mon>