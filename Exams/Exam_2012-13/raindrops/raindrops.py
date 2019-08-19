import sys

n = int(sys.stdin.readline())
num = str(sys.stdin.readline()).split(' ')

for x in range(n):
    num[x] = int(num[x])

#print n
#print num 

def raindrop(arr, x):

    sum = 0
    divisor = 0 
    for i in range(x):
        if arr[i] >= 0:
            sum += arr[i]
            divisor += 1

    if divisor <= 0:
        return "INSUFFICIENT DATA"
    else:
        return sum / divisor 


print raindrop(num, n)
