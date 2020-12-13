numb = int(input('Enter a positive integer: '))


def count(N):
    zeros, i = 0, 5
    while N / i >= 1:
        zeros += N // i
        i *= 5
    return zeros


print(f"No.of trailing zeros in {numb}! are", count(numb))
