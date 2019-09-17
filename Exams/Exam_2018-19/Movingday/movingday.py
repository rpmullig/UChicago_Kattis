import sys

tmp = str(sys.stdin.readline()).strip().split(' ')

n = int(tmp[0])
V = int(tmp[1])

arr = []
largest_i = 0

for i in xrange(n):
    tmp = str(sys.stdin.readline()).strip().split(' ')
    arr.append(int(tmp[0]) * int(tmp[1]) * int(tmp[2]))
    if arr[i] > arr[largest_i]:
        largest_i = i

print arr[largest_i] - V


    
