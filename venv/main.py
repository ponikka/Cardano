from tabulate import tabulate
from random import choice
from string import ascii_uppercase
from math import sqrt, ceil

alphabet = list(ascii_uppercase)
word = input('Enter the phrase\n')
side = ceil(sqrt(len(word)))
print(side)
if side % 2 != 0:
    side = side + 1
print(side)
square = []
square = [[0] * side for i in range(side)]

for i in range(side // 2):  # create the chiper key
    for j in range(side // 2):
        square[i][j] = 1

count = 0

for i in range(side):
    for j in range(side):
        if square[i][j] == 1:
            square[i][j] = word[count]
            count = count + 1
            square[i][side-j-1] = word[count+side]


for i in range(side):
    for j in range(side):
        value = square[i][j]
        square[i][j] = square[side-i-1][j]
        square[side-i-1][j] = value


print(tabulate(square, tablefmt='grid'))
