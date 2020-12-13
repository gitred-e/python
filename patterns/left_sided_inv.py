# Printing the foolowing pattern
# * * * * *
# * * * *
# * * *
# * *
# *


import os
os.system('cls')

num = int(input('Enter a positive number: '))

for i in range(num, 0, -1):
    for j in range(1, i+1):
        print('*', end=' ')
    print('\n')
