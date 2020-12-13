num = int(input('Enter a positive integer to know its factorial: '))
fact = 1

if num >= 0:
    for x in range(1, num+1):
        fact *= x
    print(f"{num}! is", fact)
elif num < 0:
    print('Factorial is only defined for positive integers.')
