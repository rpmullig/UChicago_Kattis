import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
pairs = []
edges = {}

# capture all the paris
for i in xrange(E):
    tmp = str(sys.stdin.readline()).replace(' ', '')
    tmp = list(tmp)
    pairs.append([int(tmp[0]), int(tmp[1])])

# create dictionaries for edge count and a visited
visited = {}
for i in xrange(V):
    visited[i] = False
    edges[i] = []

#print edges

for elm in pairs:
    edges[elm[0]].append(elm[1])
    edges[elm[1]].append(elm[0])


def dfs(graph, root):
    graph[root] = True
    for elm in edges[root]:
        tmp = graph[elm]
        if not tmp:
            dfs(graph, elm)

focus_root = 0
count = 0 

def visit_check(graph):
    for i in xrange(len(graph)):
        if not graph[i]:
            return i
    return -1

while focus_root != -1:
    dfs(visited, focus_root)
    #print visited
    focus_root = visit_check(visited)
    count += 1
	  
print count


"""
old code stored for a second
# create dictionaries for edge count and a visited
visited = {}
for i in xrange(V):
    visited[i] = False
    edges[i] = []

#print edges

for elm in pairs:
    edges[elm[0]].append(elm[1])
    edges[elm[1]].append(elm[0])


def dfs(graph, root):
    graph[root] = True
    for elm in edges[root]:
        tmp = graph[elm]
        if not tmp:
            dfs(graph, elm)

focus_root = 0
count = 0 

def visit_check(graph):
    for i in xrange(len(graph)):
        if not graph[i]:
            return i
    return -1

while focus_root != -1:
    dfs(visited, focus_root)
    #print visited
    focus_root = visit_check(visited)
    count += 1
	  
print count
"""