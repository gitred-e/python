x, y = input('Enter two numbers seperated by space: ').split()
x, y = int(x), int(y)


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def lcm(hcf, a, b):
    lcm = (a * b) / hcf
    print(f"The LCM of {a} and {b} is:", lcm)


lcm(gcd(x, y), x, y)
