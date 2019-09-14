import sys

tmp = str(sys.stdin.readline()).replace(' ', '').replace('\n', '')

tmp = list(tmp)
C = int(tmp[0])
n = int(tmp[1])
del tmp

flag = True
on_train = 0
dataSet = []
i = 0               

# train stops object to hold the data from each stop
class stops:
        def __init__(self, stop_number, exited, entered, waited):
                self.stop_number = stop_number
                self.exited = exited
                self.entered = entered
                self.waited = waited

# loops through to store each instance
while i < n:
	tmp = str(sys.stdin.readline()).replace(' ', '').replace('\n', '')
	tmp = list(tmp)
        current_stop = stops(i+1, int(tmp[0]), int(tmp[1]), int(tmp[2]))
        dataSet.append(current_stop)       
	del tmp, current_stop
        i += 1

if dataSet[0].exited > 0:
        flag = False
        
for elm in dataSet:
        on_train = on_train - elm.exited
        if on_train < 0 and flag:
                flag = False
        on_train = on_train + elm.entered
        if on_train > C and flag:
                flag = False
        if on_train < C and elm.waited > 0 and flag:
                flag = False

if on_train != 0 and flag:
        flag = False
        
if flag:
        print "possible"
else:
        print "impossible"
