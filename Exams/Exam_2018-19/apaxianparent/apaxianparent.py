import sys

tmp = str(sys.stdin.readline()).strip().split(' ')

Y = tmp[0]
P = tmp[1]


vowels = ['a', 'i', 'o','u']

if Y[-1] == 'e':
    ans = Y + 'x' + P
elif Y[-1] in vowels:
    ans = Y[0:len(Y)-1] + "ex" + P
elif Y[len(Y)-2:] == "ex":
    ans = Y + P
else:
    ans = Y + "ex" + P

print ans
