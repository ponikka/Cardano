from tabulate import tabulate
from random import choice
from string import ascii_uppercase
from math import sqrt, ceil

alphabet = list(ascii_uppercase)
word = input('Enter the phrase\n').upper()
side = ceil(sqrt(len(word)))

if side % 2 != 0:
    side = side + 1

square = []
square = [[0] * side for i in range(side)]

for i in range(side):  # create the chiper key
    for j in range(side // 2):
        square[i][j] = 1

print('The KEY:')
print(tabulate(square, tablefmt='grid'))

count = 0

for i in range(side // 2):
    for j in range(side):
        if square[i][j] == 1 and len(word) > count:
            square[i][j] = word[count]
            square[i][side - j - 1] = word[count + (side//2)*(side//2)]
            count = count + 1

count = count + count

for i in range(side // 2, side):
    for j in range(side):
        if square[i][j] == 1 and len(word) > count:
            square[i][j] = word[count]
            if len(word) > count + side:
                square[i][side - j - 1] = word[count + (side//2)*(side//2)]
            count = count + 1

print("Final table:")

for i in range(side):
    for j in range(side):
        if square[i][j] == 1 or square[i][j] == 0:
            square[i][j] = choice(alphabet)


print(tabulate(square, tablefmt='grid'))
