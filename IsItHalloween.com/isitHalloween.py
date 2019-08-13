#import module
import sys

#read stdin for input
input_ = str(sys.stdin.readline()).replace('\n', "").split(' ')
input_[1] = int(input_[1])


def isItHalloween(x):
    if (x[0] == 'OCT' and x[1] is 31):
        return "yup"
    elif (x[0] == 'DEC' and x[1] is 25):
        return "yup"
    else:
        return "Nope"

print isItHalloween(input_)
