# import module
import sys

# read stdin for input
x = str(sys.stdin.readline())
y = list(x)
y.remove('\n')
#y = ['?', '?', '?', '?', '1', '0', '1', '1', '?', '?']

#----- program logic ------

# global  variables
ans = 0

def locations(seq):
        k_locations = []
        one_locations = []
        zero_locations = []

        # put the locations in respective arrays
        for x in xrange(len(seq)): 
	        if seq[x] is '?':
		        k_locations.append(x)
	        elif seq[x] is '1':
		        one_locations.append(x)
	        elif seq[x] is '0':
		        zero_locations.append(x)
	        else: 
		        raise Exception('Not a 0, 1, or ?')
        return [one_locations, zero_locations, k_locations, len(seq), seq]


def seq_generator(locs):

        swap_count = 0
        
        for x in xrange(2**len(locs[2])):
                holder = locs[4]
                k_holder = list(format(x,'#0'+str(len(locs[2])+2)+'b')[2:])

                for k in xrange(len(locs[2])):
                        holder[locs[2][k]] = k_holder.pop()
                        
                swap_count = swap_counter(holder) + swap_count
                #print locations(holder)
                        
        return swap_count

def swap_counter(seq_filled):
        counter = 0
        calculations = locations(seq_filled)
        for x in reversed(xrange(len(calculations[1]))):
                        if len(calculations[0]) is 0:
                                return counter

                        if calculations[1][x] > calculations[0][0]:
                                counter = calculations[1][x] - calculations[0][0]
                                calculations[0] = calculations[0][1:]
                       # print calculations
        return counter

#print locations(y)
print (seq_generator(locations(y)) % (10**9 +7))

