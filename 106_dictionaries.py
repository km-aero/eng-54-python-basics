# Dictionaries
# work with key and value pairs

# Syntax
dict_ = {'key1':'value1',
         'key2':'value2'}

boris_dict = {
    'name': 'Boris',
    'l_name': 'Johnson',
    'phone': '0784171157',
    'address': '10 Downing Street'
}

# Access one key value pair
boris_dict['phone']

# change value of one key value pair
boris_dict['l_name'] = 'Bob'
print(boris_dict['l_name'])

# assign new key value pair

boris_dict['new_key'] = 'no idea'

# get all keys
print(boris_dict.keys())

# get all values
print(boris_dict.values())