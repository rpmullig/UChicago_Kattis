import sys

x = list(str(sys.stdin.readline()))

def Trik(arr):
    ans = [1, 0, 0]
    
    for elm in arr:
        if elm is 'A':
            ans = swap(ans, 0, 1)
        elif elm is 'B':
            ans = swap(ans, 1, 2)
        elif elm is 'C':
            ans = swap(ans, 0, 2)

    for x in xrange(len(ans)):
        if ans[x] == 1:
            return x+1


def swap(arr, pos_1, pos_2):
    temp = arr[pos_1]
    arr[pos_1] = arr[pos_2]
    arr[pos_2] = temp
    return arr


print Trik(x) 
