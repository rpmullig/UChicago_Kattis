import sys

n = str(sys.stdin.readline()).replace("\n", "")
n = int(n)

tmp = str(sys.stdin.readline()).replace("\n","").split(' ')
bats = []

for elm in tmp:
    bats.append(int(elm))

sum = 0.0
for elm in bats:
    if elm == -1:
        n -= 1
    else:
        sum += elm

print sum / n
