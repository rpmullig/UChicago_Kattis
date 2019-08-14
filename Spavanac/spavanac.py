import sys

X = str(sys.stdin.readline()).replace('\n', '').split(' ')

H = int(X[0])
M = int(X[1])


def spavanac(H, M):
    M  = (H*60) + M
    if M > 45:
        M = M - 45
    else:
        M = M + 24*60 - 45

    H = M / 60
    M = M % 60

    return str(H) + " " + str(M)

print spavanac(H, M)
