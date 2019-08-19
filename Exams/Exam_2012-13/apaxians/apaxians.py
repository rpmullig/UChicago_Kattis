import sys

word = str(sys.stdin.readline())

sum = 0
if len(word) > 0:
    first_letter = word[0]
    for x in xrange(len(word)):
        if word[x] is first_letter:
            sum += 1

print sum
