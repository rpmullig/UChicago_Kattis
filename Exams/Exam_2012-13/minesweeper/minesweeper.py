import sys

input_s = str(sys.stdin.readline()).split(' ')
r = int(input_s[0])
c = int(input_s[1])
del input_s

matrix = []
mines = []

for x in xrange(r):
    input_s = str(sys.stdin.readline()).split(' ')
    temp = []
    for y in xrange(c):
        if int(input_s[y]) is 1:
            temp.append('X')
            mines.append([x, y])
        else:
            temp.append(int(input_s[y]))
    matrix.append(temp)

#def
# print matrix

def pretty_print(mat):
    for row in xrange(len(mat)):
        temp_str = ""
        for col in xrange(c):
            temp_str += str(mat[row][col]) 
        print temp_str


def in_bound(mat, x, y):
    if y >= len(mat[0]) or y < 0:
        return False
    elif x >= len(mat) or x < 0:
        return False
    elif mat[x][y] is 'X':
        return False
    else:
        return True

def mine_locations(mat, mines):
    for cord in mines:
       # print cord
       # pretty_print(matrix) 
        temp_x = cord[0]
        temp_y = cord[1]
        # left
        if in_bound(mat, temp_x - 1, temp_y):
            mat[temp_x - 1][temp_y] += 1
        # down left
        if in_bound(mat, temp_x - 1, temp_y - 1):
            mat[temp_x - 1][temp_y - 1] += 1
        # down
        if in_bound(mat, temp_x, temp_y - 1):
            mat[temp_x][temp_y - 1] += 1
        # down right
	if in_bound(mat, temp_x + 1, temp_y - 1):
            mat[temp_x + 1][temp_y - 1] += 1
        # right
        if in_bound(mat, temp_x + 1, temp_y):
            mat[temp_x + 1][temp_y] += 1
        # up right
        if in_bound(mat, temp_x + 1, temp_y + 1):
            mat[temp_x + 1][temp_y + 1] += 1
        # up 
        if in_bound(mat, temp_x, temp_y + 1):
            mat[temp_x][temp_y + 1] += 1
        # up left 
        if in_bound(mat, temp_x - 1, temp_y + 1):
            mat[temp_x - 1][temp_y + 1] += 1
    for row in xrange(r):
        for col in xrange(c):
            if mat[row][col] == 0:
                mat[row][col] = '-'


mine_locations(matrix, mines)
pretty_print(matrix)
