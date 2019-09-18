import sys

[N, R, H, M, S] = sys.stdin.readline().strip().split(' ')

N = int(N)
R = int(R)
H = int(H)
M = int(M)
S = int(S)

cities = {}

for i in xrange(N):
    tmp = sys.stdin.readline().strip().split(' ')
    cities[tmp[1]] = [int(tmp[0]), int(tmp[2])]

roads = {}

for i in xrange(R):
    tmp = sys.stdin.readline().strip().split(' ')
    roads[tmp[1]] = [int(tmp[0]), int(tmp[1])]


print cities
print roads
