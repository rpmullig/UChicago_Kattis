import sys

[A, B] = str(sys.stdin.readline()).strip().split(' ')

tmpA = ""
tmpB = ""

for char in A:
    tmpA = char + tmpA

for char in B:
    tmpB = char + tmpB

A = int(tmpA)
B = int(tmpB)



if A > B:
    print A
else:
    print B

