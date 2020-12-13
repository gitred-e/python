# Printing the number of fibonacci numbers the user want

import os

os.system('cls')

num = int(input('Enter number of fibonacci numbers you want:'))
count = 2
a, b = 0, 1
c = a + b
print(b, c, end=' ')
while count < num:
    a = b
    b = c
    c = a + b
    print(c, end=' ')
    count += 1
