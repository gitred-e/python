# Printing the following pattern
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

import os
os.system('cls')

num = int(input('Enter a positive number: '))

for i in range(1, num+1):
    for j in range(i, num):
        print(' ', end=' ')
    for k in range(1, i+1):
        print('*', end=' ')
    for l in range(1, i):
        print('*', end=' ')
    print('\n')

for i in range(1, num):
    for j in range(1, i+1):
        print(' ', end=' ')
    for k in range(i, num):
        print('*', end=' ')
    for l in range(i, num-1):
        print('*', end=' ')
    print('\n')
