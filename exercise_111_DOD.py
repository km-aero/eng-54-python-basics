# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate responses as I go

while True:
    question = str(input('What is your question trainee?\n'))
    print('questions are wise, but for now. Wax on, wax off!')
    split_question = question.split()
    question = question.lower()

    if 'sensei' not in split_question[0].lower():
        print('You are smart, but not wise - address me as Sensei please')

    elif ('block' in question) or ('blocking' in question):
        print('Remember, best block, not to be there..')

    elif 'Sensei, I am at peace'.lower() == question:
        print('Sometimes, what heart know, head forget')
        break

    else:
        print('Do not lose focus. Wax on. Wax off.')



# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remember, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')