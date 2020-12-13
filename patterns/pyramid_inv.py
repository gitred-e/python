# Printing the following pattern
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

import os
os.system('cls')

num = int(input('Enter a number: '))

for i in range(1, num+1):
    for j in range(1, i):
        print(' ', end=' ')
    for k in range(i, num+1):
        print('*', end=' ')
    for l in range(i, num):
        print('*', end=' ')
    print('\n')
