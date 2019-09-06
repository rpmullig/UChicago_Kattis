import sys

fhand = sys.stdin
N = int(str(fhand.readline()).replace('\n', "").split(' ')[0])
arr = list()

for i in xrange(N):
    temp = str(fhand.readline().replace('\n', "")).split(' ')
    q = float(temp[0])
    y = float(temp[1])
    arr.append([q, y])

del temp

qaly = 0.0

for elm in arr:
    qaly += (elm[0] * elm[1])


    
print("{0:.3f}".format(round(qaly, 3)))
