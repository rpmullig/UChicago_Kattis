# import module
import sys

# read stdin for input
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

def quadrant(x, y):

    if(x > 0 and y > 0): return 1
    elif(x < 0 and y > 0): return 2
    elif(x < 0 and y < 0): return 3
    else: return 4

print quadrant(x, y)
