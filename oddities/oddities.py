import sys

n = int(str(sys.stdin.readline()).strip())

for i in xrange(n):
    tmp = int(str(sys.stdin.readline()).strip())
    if tmp % 2 == 0:
        print("%d is even" %(tmp))
    else:
        print("%d is odd" %(tmp))

