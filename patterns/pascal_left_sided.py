# Printing the following pattern
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

import math as m
import os
os.system('cls')

num = int(input('Enter a positive number: '))

for row in range(0, num):
    for col in range(0, row + 1):
        print(m.comb(row, col), end=' ')
    print('\n')
