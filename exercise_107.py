# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []

i = 0
for i in range(len(menu)):
    menu[i] = menu[i].capitalize()
    print(menu[i])

i = 0
while i < 3:
    food_order.append(input('What would you like to order?\n'))
    i += 1

i = 0
print('So you want:')
for i in range(len(food_order)):
    food_order[i] = food_order[i].capitalize()
    print(food_order[i])


# I need to print each item from the list

# before I print I need to make them all capitalized
#  print everything