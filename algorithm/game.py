N, M = map(int, input().split())

# initialization for the game
d = [[0] * M for _ in range(N)
X, Y, direction = map(int, input().split())
d[X][Y] = 1

# input the map
array = []
for i in range(N):
    array.append(list(map(int, input().split())))
    
# print(array)
# print(d)
        
# define the direction (North, East, South, West)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# turn left function
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# start the game
count = 1
turn_time = 0

while True :
    # turn left
    turn_left()
    nx = X + dx[direction]
    ny = Y + dy[direction]
    
    # if the next position is not visited and not a wall
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        X = nx
        Y = ny
        count += 1
        turn_time = 0
        continue # go to the next iteration
    # if the next position is visited or a wall
    else :
        turn_time += 1
        
    if turn_time == 4 :
        nx = X - dx[direction]
        ny = Y - dy[direction]
        
        # if backward available :
        if array[nx][ny] == 0:
            X = nx
            Y = ny
        # if backward not available :
        else :
            break
            
        turn_time = 0
        
print(count)