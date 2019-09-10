import sys

# take in input integers as strings
num1 = str(sys.stdin.readline())
num2 = str(sys.stdin.readline())

num1 = num1[:len(num1)-1]
num2 = num2[:len(num2)-1]

#print num1
#print num2

while len(num1) < len(num2):
	num1 = '0' + num1
while len(num2) < len(num1):
	num2 = '0' + num2

#print num1
#print num2

ans_num1, ans_num2 = "", ""


i = 0
while i < len(num2):
	if int(num1[i]) > int(num2[i]):
		ans_num1 += num1[i]
	elif int(num1[i]) < int(num2[i]):
		ans_num2 += num2[i]
	else:
		ans_num1 += num1[i]
		ans_num2 += num2[i]
	i += 1


if ans_num1 is "":
	print "YODA"
else:
	print int(ans_num1)

if ans_num2 is "":
    print "YODA"
else:
    print int(ans_num2)
