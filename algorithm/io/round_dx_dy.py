n, m = map(int, input().split())

grid = [[0 for i in range(m)] for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cur_dir = 0

grid[0][0] = 1
x, y = 0, 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n*m + 1) : 
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    # out of range or already visited :
    if not in_range(nx, ny) or grid[nx][ny] != 0 :
        cur_dir = (cur_dir + 1) % 4
    
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    x, y = nx, ny
    grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(grid[i][j], end= " ")
    print()