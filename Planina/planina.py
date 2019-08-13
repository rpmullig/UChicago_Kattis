# import module
import sys

# read stdin for input
x = int(sys.stdin.readline())

def Planina(z):
    return helper(z)**2

def helper(y):
    sides = 2
    
    while(y > 0):
        sides = sides + 2**(y-1)
        y = y - 1

    return sides

    
print Planina(x) 
