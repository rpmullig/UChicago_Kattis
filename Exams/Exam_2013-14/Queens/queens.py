import sys

N = int(sys.stdin.readline())
queens = []

for i in xrange(N):
    temp = str(sys.stdin.readline()).split(' ')
    temp_arr = [ int(temp[0]), int(temp[1])]
    queens.append(temp_arr)
    del temp
    del temp_arr

matrix = []

for row in xrange(N):
    matrix.append([0] * N)
    

def pretty_print(mat):
    for row in xrange(len(mat)):
        print mat[row]


def queen_path(mat, x, y):
    for i in xrange(N):
        if mat[x][i] = 1 and i is not y:
            return False


for elm in queens:
    x = elm[0]
    y = elm[1] 
    matrix[x][y] = 1
    queen_path(matrix, x, y)

    del x
    del y



