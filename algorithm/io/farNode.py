n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] 

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append([e[1]])
        graph[e[1]].append([e[0]])
        
    for g in graph:
        g.sort()
        
    visited = [0] * (n+1)
    def bfs(graph, v, visited):
        queue = deque()
        queue.append(v)
        visited[v] = 1
        while queue :
            n = queue.popleft()
            for i in graph[n] : 
                if visited[i[0]] == 0 :
                    visited[i[0]] = visited[n] + 1 # 이전 노드값 보다 1 크게
                    queue.append(i[0])
        return max(visited)
    
    m = bfs(graph, 1, visited)
    
    return visited.count(m)

print(solution(n, edge))