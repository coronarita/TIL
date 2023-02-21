n = int(input())
mov = list(input().split())

# L R U D
dir = {'L':0, 'R':1, 'U':2, 'D':3}
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 0, 0
for m in mov : 
    nx = x + dx[dir[m]]
    ny = y + dy[dir[m]]
    if 0 <= nx < n and 0 <= ny < n :
        x, y = nx, ny
print(x+1, y+1)