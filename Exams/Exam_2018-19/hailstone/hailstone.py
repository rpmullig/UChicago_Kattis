import sys

n = str(sys.stdin.readline()).strip()
n = int(n)

def hailstone(x):
    global ans
    if x == 1:
        return 1
    elif x % 2 == 0:
        tmp = x/2
        return x + hailstone(tmp)
    else:
        tmp = 3*x+1
        return x + hailstone(tmp)


ans = hailstone(n)
print ans
