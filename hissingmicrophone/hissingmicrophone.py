import sys

input_ = str(sys.stdin.readline())

def justine(input_):
    # base case where only 1 character
    if len(input_) == 1: return "no hiss"

    for x in xrange(1, len(input_)):
        if input_[x] is input_[x-1] and input_[x] is 's':
                return "hiss"

    return "no hiss"

print justine(input_)
