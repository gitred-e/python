# Printing the following pattern
# 1
# 1 1
# 1 2 1
# 1 2 3 1
# 1 2 3 4 1

import os
os.system('cls')

num = int(input('Enter a positive number: '))

for i in range(0, num):
    for j in range(1, i+1):
        print(j, end=' ')
    print('1\n')
