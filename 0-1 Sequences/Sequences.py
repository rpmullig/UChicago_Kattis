# import module
import sys

# read stdin for input
x = str(sys.stdin.readline())
y = list(x)
y.remove('\n')

#----- program logic ------

ans = 0
k_count = 0

for elm in y:
        if elm is '?':
                k_count = k_count + 1










'''
                def solver_r(input, ans):
        for x in xrange(len(input)):
               
                print (input)
        
                if input[x] is  '?':
                        one_input = input[:]
                        one_input[x] = '1'
                        ans = ans + solver_r(one_input, 0)
                        zero_input = input[:]
                        zero_input[x] = '0'
                        ans = ans + solver_r(zero_input, 0)

                elif input[x] is '1' and x+1 is not len(input) and input[x+1] is '0':
                        ans = ans + 1
                        input[x] = '0'
                        input[x+1] = '1'
                        #  ans = ans + solver_r(swap_input, 0)
        return ans


        
print(solver_r(y, 0)  % (10**9 +7))

'''
