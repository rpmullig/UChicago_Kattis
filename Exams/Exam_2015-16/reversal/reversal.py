import sys

r = str(sys.stdin.readline())


def reversal(word):
    if len(word) == 1:
        return word
    else:
        return  reversal(word[1:]) + word[0:1]

ans = reversal(r)

print ans
