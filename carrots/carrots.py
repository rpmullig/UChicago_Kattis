import sys

fhand = sys.stdin

temp = str(fhand.readline()).replace('\n', '').split(' ')
N = int(temp[0])
P = int(temp[1])
del temp

print P
