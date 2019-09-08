import sys

# take in input integers as strings
num1 = str(sys.stdin.readline())
num2 = str(sys.stdin.readline())

# put digits in a arrays as string characters
num1_arr, num2_arr = [char for char in num1], [char for char in num2]

# remove the '\n' for next line
num1_arr.pop()
num2_arr.pop()

# make the arrays equal length for comparison by adding 0's in front
if len(num1) > len(num2):
    tmp = [ '0' * (len(num1)-len(num2))]
    num2_arr = tmp + num2_arr
elif len(num2) > len(num1):
    tmp =  [ '0' * (len(num2)-len(num1))]
    num1_arr = tmp + num1_arr

#print num1_arr
#print num2_arr
# create a compare function to be used for logic in subsequent while loop
def compare(digit1, digit2, i):
    digit1 = int(digit1)
    digit2 = int(digit2)
    if digit1 == digit2:
        return
    elif digit1 > digit2:
        num2_arr[i] = None
        return
    elif digit2 > digit1:
        num1_arr[i] = None
        return

# now combine and print
num1 = ""
num2 = ""

for x in xrange(min(len(num1_arr), len(num2_arr))):
   compare(num1_arr[x], num2_arr[x], x)
   if num1_arr[x] is not None:
       num1 += num1_arr[x]

   if num2_arr[x] is not None:
       num2 += num2_arr[x]


if num1 is '':
    print "YODA"
else:
    print int(num1)

if num2 is '':
    print "YODA"
else:
    print int(num2)
