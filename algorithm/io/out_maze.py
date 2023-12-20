n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# directions : UDLR
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# using BFS
def BFS(x, y) : 
    from collections import deque
    dq = deque()
    dq.append((x, y))
    # 큐가 빌 때까지 반복 수행
    while dq : 
        x, y = dq.popleft()
        # 현재 방향에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 공간 벗어날 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m : 
                continue
            # 벽/괴물 인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우, 최단거리를 기록
            if graph[nx][ny] == 1 : 
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))
                
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


print(BFS(0,0))    
    
