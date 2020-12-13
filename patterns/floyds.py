# Printing the following pattern (Floyds Triangle)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

import os
os.system('cls')

num = int(input('Enter a positive number: '))
temp = 1

for i in range(1, num+1):
    for j in range(1, i+1):
        print(temp, end=' ')
        temp += 1
    print('\n')
