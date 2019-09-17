import sys

N = int(str(sys.stdin.readline()).replace("\n", ''))

numerator = 0.0
denominator = 0.0

for i in xrange(N):
    tmp = str(sys.stdin.readline()).replace("\n",'')
    for char in tmp:
        if char is 'C' or char is 'G':
            numerator += 1
            denominator += 1
        else:
            denominator += 1

print ((numerator / denominator) * 100)
