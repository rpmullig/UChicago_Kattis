import sys

x = str(sys.stdin.readline())

def autori(string):
    ans = string[0]
    flag = int(0)
    
    for elm in string:
        if flag:
            ans = ans + elm

        if elm is '-':
            flag = 1
        else:
            flag = 0

    return ans

print autori(x) 
