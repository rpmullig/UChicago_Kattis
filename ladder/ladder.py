import sys, math

[h, v] = str(sys.stdin.readline()).strip().split(' ')

h = int(h)
v = int(v)
#v needs to be in radians
v = (math.pi/180)*v


print int(math.ceil(h / math.sin(v)))
