import os
os.system('cls')

num = int(input('Enter a positive number:'))

for i in range(1, num + 1):
    for j in range(i, num):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(chr(64 + i), end=' ')
    for l in range(1, i):
        print(chr(64+i), end=' ')
    print('\n')
