# 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()
# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# check move_plans
for plan in plans:
    # check with move_types
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    # check nx, ny
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    # update x, y
    x = nx
    y = ny
    
print(x, y)
    
