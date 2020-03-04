# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


while True:
    num = input('Please enter a number\n')

    if 'penpinapplespen' in num:
        print('Thank you for playing. Bye!')
        break

    for i in range(int(num)):
        composite = ''
        if ((i+1)%3) == 0:
            composite = 'bizz'
        if ((i+1)%5) == 0:
            composite += 'zzuu'
        print(i+1, composite)

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu