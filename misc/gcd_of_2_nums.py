num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))


def gcd(x, y):
    while (x != y):
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


if num1 != num2:
    result = gcd(num1, num2)
    print(f'GCD of {num1} and {num2} is', result)
elif num1 == num2:
    print('GCD is', num1)
