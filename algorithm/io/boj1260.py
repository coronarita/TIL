# dfs, bfs
# 1. make graph using loop
# 2. using two stack, queue (visited, stack/queue)
# 3. start with first node
# 4. insert in stack, queue (while queue)
# 5. if key is not in visited - insert on visited, insert values at stack /queue
# 6 . if not : pass
# 7. repeat 4 to 7 

from collections import deque, defaultdict

def bfs(g, v): # queue, FIFO
    queue = deque()
    queue.append(v)
    
    while(queue):
        node = queue.popleft()
        if node not in visited : 
            visited.append(node)
            queue.extend(g[node])

    return visited

def dfs(g, v): # stack LIFO
    queue = deque()
    queue.append(v)
    
    while(queue):
        node = queue.pop()
        if node not in visited : 
            visited.append(node)
            for component in g[node]:
                if component not in visited :            
                    dfs(g, component)

    return visited


n, m, v = map(int, input().split())

# make graph using input information

graph = defaultdict(list)
new = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for key, val in graph.items():
    graph[key].sort()    
new_graph = sorted(graph.items(), key=lambda x : x[0])

for comp in new_graph:
    # print(comp)
    new[comp[0]] = comp[1]
    # graph[comp[0]].extend(new_graph[comp[0]])

# print(new)
visited = []
print(*dfs(new, v))
visited = []
print(*bfs(new, v))