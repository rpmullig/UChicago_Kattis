import sys

n = int(str(sys.stdin.readline()).strip())

for i in xrange(n):
    [r, e, c] = str(sys.stdin.readline()).strip().split(' ')
    r = int(r)
    e = int(e)
    c = int(c)

    if r < e - c:
        print "advertise"
    elif r > e - c:
        print "do not advertise"
    else:
        print "does not matter"

