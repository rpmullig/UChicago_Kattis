import sys

tmp = str(sys.stdin.readline()).split(' ')

a = int(tmp[0])
b = int(tmp[1])
c = int(tmp[2])

del tmp 

ans_arr = [ "Format #1", "Format #2", "Format #3", "Ambiguous"]
x = 0

if a > 31:
    x = 2
elif a > 12 and a <= 31:
    if c > 31:
        x = 1
    elif c <= 31:
        x = 3
elif a <= 12:
    if b > 12:
        x = 0
    elif b <= 12:
        x = 3

print ans_arr[x]

