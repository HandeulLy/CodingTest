import sys

# DFS
def dfs(graph, root) :
    visited = []
    stack = [root]    
    while stack :
        vertex = stack.pop()        
        if vertex not in visited :
            visited.append(vertex)
            if vertex not in graph : return [vertex]
            else :
                for node in sorted(graph[vertex], reverse=True) :
                    if node not in visited :
                        stack.append(node)                    
    return visited

# BFS
def bfs(graph, root) :
    visited = []
    queue = [root]
    visited.append(root)
    while queue :
        vertex = queue.pop(0)
        if vertex not in graph : return [vertex]
        else :
            for node in sorted(graph[vertex]) :
                if node not in visited :
                    queue.append(node)    
                    visited.append(node)   
    return visited
'''
# input 
vertices, edges, root = map(int, input().split())
graph = {}

# create grage

for i in range(edges) :
    vertexA, vertexB = map(int, input().split())
    if vertexA not in graph : graph[vertexA] = [vertexB]
    else : graph[vertexA] += [vertexB]
    
    if vertexB not in graph : graph[vertexB] = [vertexA]
    else : graph[vertexB] += [vertexA]
'''

# output
'''
print()
print(' '.join(map(str,dfs(graph, root))))
print(' '.join(map(str,bfs(graph, root))))
'''
'''
result_dfs = dfs(graph, root)
for i in range(len(result_dfs)) :
    print("{} ".format(result_dfs[i]), end='')

print()
result_bfs = bfs(graph, root)
for i in range(len(result_bfs)) :
    print("{} ".format(result_bfs[i]), end='')
'''
aaa = ['a', 'b', 'c']
bbb = aaa.copy()
print(aaa, bbb)
aaa[0] = 'd'
print(aaa, bbb)
