# Printing the prime numbers in the given range

import os
import math

os.system('cls')

ls = []

slimit = int(input('Enter a start limit: '))
elimit = int(input('Enter an end limit: '))

for i in range(slimit, elimit + 1):
    if i == 1:
        pass
    elif i > 2 and i % 2 == 0:
        pass
    else:
        for j in range(3, math.isqrt(i) + 1, 2):
            if i % j == 0:
                break
        else:
            ls.append(i)

print(f"List of primes between {slimit} and {elimit} are:")
print(ls, '=', len(ls), '\n')
