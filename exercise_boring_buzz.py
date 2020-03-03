#specs:
# multiples of 3 --> boring
# multiples of 5 --> buzz
# multiples of 3 and 5 --> boringbuzz

num = int(input('Enter a number'))

if (num%3)==0:
    print("boring")

if (num%5)==0:
    print("buzz")