n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# checking visited info
d = [[0]* m for _ in range(n)]

d[x][y] = 1 # current position

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left() : 
    global direction
    direction -= 1
    if direction == -1:
        direction = 3 
        
# simulation
count = 1
turn_count = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else : 
        turn_count += 1
        if turn_count == 4 :
            # go back 
            nx = x - dx[direction]
            ny = y - dy[direction]
            
            if array[nx][ny] == 0 :
                x = nx
                y = ny
            else :
                break
            turn_count = 0

print(count)
            
            

