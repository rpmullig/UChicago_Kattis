import sys

winner = 0
biggest = 0
tmp_compare = 0

for i in xrange(5):
    tmp = str(sys.stdin.readline()).strip().split(' ')
    for elm in tmp:
        elm = int(elm)
        tmp_compare += elm
    if tmp_compare > biggest:
        winner = i + 1
        biggest = tmp_compare
    del tmp
    tmp_compare = 0

print ("%d %d" %(winner, biggest))
