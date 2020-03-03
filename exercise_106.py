# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
magic_number = 21

# I need to ask user for input
num = int(input('Whats the magic number?'))

# I need to check if this input matches a magic_number
if num == magic_number:
    print('Right!!! (Self Five)')
else:
    print('Wrong!!!!')

# I need to let the user know if the response was write or not
#self five