import sys

T = int(str(sys.stdin.readline()).strip())

for i in xrange(T):
    destinations = {}
    trips = int(str(sys.stdin.readline()).strip())
    for x in xrange(trips):
        tmp = str(sys.stdin.readline()).strip()
        destinations[tmp] = 1
    print len(destinations.keys())
