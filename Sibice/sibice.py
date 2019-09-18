import sys, math

[N, W, H] = str(sys.stdin.readline()).strip().split(' ')

N = int(N)
W = int(W)
H = int(H)

max_length = math.sqrt(W**2 + H**2)

for i in xrange(N):
    tmp = str(sys.stdin.readline()).strip()
    tmp = int(tmp)
    if tmp > max_length:
        print "NE"
    else:
        print "DA"

