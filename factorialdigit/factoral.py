import sys

N = int(str(sys.stdin.readline()).strip())

def factoral(y):
    if y > 1:
        return y * factoral(y-1)
    else:
        return 1


for i in xrange(N):
    x = int(str(sys.stdin.readline()).strip())
    print factoral(x) % 10
