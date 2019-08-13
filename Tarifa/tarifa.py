import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sum = X

for y in xrange(N):
    sum = sum + (X - int(sys.stdin.readline()))


print sum
