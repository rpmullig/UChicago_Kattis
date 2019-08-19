import sys

x = str(sys.stdin.readline()).split(' ')
a = int(x[0])
b = int(x[1])
del x 


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(a, b - a)

print gcd(a, b)
