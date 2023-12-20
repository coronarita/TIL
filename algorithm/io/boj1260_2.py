from collections import deque

n, m, v = map(int, input().split())

# using matrix (referred)
visited_dfs = [0]* (n+1)
visited_bfs = [0]* (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v): # recursive    
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited_dfs[i] == 0 :
            dfs(i)

# def dfs(v): # stack - 작은 순서대로 되지 않음 (pop)
#     q = deque()
#     visited_dfs[v] = 1
#     q.append(v)
#     while q :
#         # 꺼내서
#         v = q.pop()
#         # 방문한 적이 없다면 방문처리 (간선이 존재해야)
#         print(v, end=" ")
#         for i in range(1, n+1):
#             if graph[v][i] == 1 and visited_dfs[i] == 0 :
#                 visited_dfs[i] = 1    
#                 q.append(i)
                
def bfs(v): # queue
    q = deque()
    visited_bfs[v] = 1
    q.append(v)
    while q :
        # 꺼내서
        v = q.popleft()
        # 방문한 적이 없다면 방문처리 (간선이 존재해야)
        print(v, end=" ")
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited_bfs[i] == 0 :
                visited_bfs[i] = 1
                q.append(i)
                
                 

dfs(v)
print()
bfs(v)