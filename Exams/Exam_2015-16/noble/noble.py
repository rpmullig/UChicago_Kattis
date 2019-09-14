import sys

name = str(sys.stdin.readline()).replace('\n', '').split(' ')


if len(name[1]) == 5:
    ans = name[1] * 4
else:
    ans = name[1] * len(name[1])


ans = name[0] + ' ' + ans

print ans
