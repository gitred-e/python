# Printing the following pattern
# ABCDEFGGFEDCBA
# ABCDEF  FEDCBA
# ABCDE    EDCBA
# ABCD      DCBA
# ABC        CBA
# AB          BA
# A            A

import os
os.system('cls')

num = int(input('Enter a positive value:\n'))

for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    for k in range(0, (num - i) * 2):
        print(' ', end='')
    for l in range(i, 0, -1):
        print(chr(64 + l), end='')
    print('\n')
