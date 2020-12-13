# Printing the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

import os
os.system('cls')

num = int(input('Enter a positive number: '))

for i in range(1, num+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print('\n')
