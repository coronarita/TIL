n = int(input())
# R U L D
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

x, y = n//2, n//2
d = 0
grid[x][y] = 1

def in_range(x, y):
    return 0<= x < n and 0<= y < n

for i in range(2, n**2 + 1):
    for j in range(1, n-1): # d를 유지해 갈 횟수
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny) or grid[nx][ny]!=0 :     
        # # nx, ny = x + dxs[d], y + dys[d]
        #     d = (d+1)%4

        grid[nx][ny] = i
        x, y = nx, ny
        # d = (d+1)%4

for g in grid:
    print(*g)

