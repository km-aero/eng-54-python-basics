# Nest data structures

crazy_landl_1 = {
    'name': 'Boris',
    'phone': '09887656789',
    'address_of_rent': '10 Chelsea',
    'age': 55
}

crazy_landl_2 = {
    'name': 'Filipe',
    'phone': '035192747489',
    'address_of_rent': 'Comporta, Portugal',
    'age': 28
}

nested_dictionary = {'boris': crazy_landl_1,
                     'filipe': crazy_landl_2
                     }
#print(nested_dictionary.values())

for i in nested_dictionary:
    print(i)
    for j in nested_dictionary[i]:
        print(j, nested_dictionary[i][j])