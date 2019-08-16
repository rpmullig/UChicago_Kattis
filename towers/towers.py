 import sys

M = int(sys.stdin.readline())
str_arr = []
int_arr = []

for i in range(0, M):
    str_arr.append(str(sys.stdin.readline()).replace('\n', ''))
    int_arr.append(eval(str_arr[i].replace('^', '**')))

#print str_arr
#print int_arr

#print "--- function call ----"

def insertion_sort(arr, arr_s, n):
    if n <= 1:
        return

    insertion_sort(arr, arr_s, n-1)

    last = arr[n-1]
    last_s = arr_s[n-1]
    j = n - 2

    while(j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        arr_s[j+1] = arr_s[j]
        j  = j - 1

    arr[j+1] = last
    arr_s[j+1] = last_s

insertion_sort(int_arr, str_arr, len(int_arr))
#print str_arr
#print int_arr

print "Case 1:"
for elm in str_arr:
    print elm
