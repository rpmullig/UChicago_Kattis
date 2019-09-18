import sys

N = str(sys.stdin.readline()).strip()
N = int(N)

X = 0

for i in xrange(N):
    tmp = str(sys.stdin.readline()).strip()
    power = int(tmp[-1])
    number = int(tmp[:len(tmp)-1])
    X += number**power

print X
    
