import sys

M = int(sys.stdin.readline())
str_arr = []
int_arr = []

for i in range(0, M):
    str_arr.append(str(sys.stdin.readline()).replace('\n', ''))
    int_arr.append(eval(str_arr[i].replace('^', '**')))

def partition(arr, str_arr, low, high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    str_arr[i+1],str_arr[high] = str_arr[high],str_arr[i+1] 
	
    return ( i+1 ) 
  
def quickSort(arr, str_arr, low, high): 
    if low < high: 
  
        pi = partition(arr, str_arr, low, high) 
  
        quickSort(arr, str_arr, low, pi-1) 
        quickSort(arr, str_arr, pi+1, high)


quickSort(int_arr, str_arr, 0, len(int_arr) - 1)


print "Case 1:"
for elm in str_arr:
    print elm
