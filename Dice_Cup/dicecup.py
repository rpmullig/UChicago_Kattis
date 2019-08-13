import sys

x = str(sys.stdin.readline()).replace('\n', "").split(' ')

x[0] = int(x[0])
x[1] = int(x[1])

def die_roll(rolls):
    arr = [0] * (rolls[0] + rolls[1])

    for x in xrange(rolls[0]):
        for y in xrange(rolls[1]):
            arr[x+y] = arr[x+y] + 1


    max = 0
    for elm in arr:
        if elm > max:
            max = elm

    for x in xrange(len(arr)):
        if arr[x] == max:
            print x+2

    return

die_roll(x)
