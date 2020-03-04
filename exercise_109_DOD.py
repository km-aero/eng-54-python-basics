while True:
    age = int(input('What is your age? (Write exit to end)\n'))
    driver_lisence = bool(input('Do you have a drivers licence? (Y/N) (Write exit to end)\n'))

    if (age >= 18) and (driver_lisence == True):
        print('You can vote and drive')

    elif (age >= 16) and (age < 18):
        print('you can\'t legally drink but your mates/uncles might have your back')

    elif (age >= 18):
        print('You can vote')

    elif driver_lisence == True:
        print('You can drive')

    elif (age < 18):
        print('You\'re too young, go back to school!')

    elif (age == 'exit') or (driver_lisence == 'exit'):
        break

    else:
        print('No idea mate')



# - You can vote and drive
# - You can vote
# - You can drive
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!