import sys

tmp = str(sys.stdin.readline()).replace("\n", "").split(' ')

N = int(tmp[0])
M = int(tmp[1])

students = {}
student_totals = [0 * N]
student_lowest = [6 * N]

for i in xrange(N):
    tmp = str(sys.stdin.readline()).replace("\n", "").split(' ')
    students[tmp[0]] = []
    for x in xrange(M):
        if x != 0 and x != M:
            #print tmp[x]
            students[tmp[0]].append(int(tmp[x]))
            

print students
