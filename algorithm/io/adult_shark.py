'''
boj 19237
'''

n, m, k = map(int, input().split())

# array : 상어의 위치(x번 상어)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))    

# print(array)

# direction
directions = list(map(int, input().split()))

# smell : 특정 냄새 - 상어 번호, 남은 시간
smell = [[[0,0]]* n for i in range(n)]

# priorities : 상어들의 방향정보 우선순위 (UDLR)

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))
    # print(priorities[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell():
    # check position
    for i in range(n):
        for j in range(n):
            # 냄새 존재 - 시간 1 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어 존재 - 냄새 k값으로 셋팅
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]
        # print(smell[i])
    
    
def move():
    # 이동결과 - new_array
    new_array = [[0]*n for _ in range(n)]
    # 위치 체크하면서 
    for x in range(n):
        for y in range(n):
            # 상어 존재
            if array[x][y] != 0: # 1,2,3,4
                direction = directions[array[x][y]-1]
                # print(direction)
                found = False
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]
                    
                    if 0<= nx < n and 0 <= ny < n:
                        # 냄새 존재하지 않으면
                        if smell[nx][ny][1] ==0 :
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]
                            
                            # 다른 상어 있다면 낮은 상어 들어가도록
                            # 이동
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else :
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                
                # 주변에 냄새가 남아있다면, 자신의 냄새로
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]
                    
                    if 0<= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == array[x][y] : # 자신의 냄새라면 
                            # 방향 이동하기
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]
                            
                            # 상어 이동
                            new_array[nx][ny] = array[x][y]
                            break
                # pass
                
    
    
    return new_array

time = 0
while True :
    update_smell()
    new_array = move()
    array = new_array
    time += 1
    
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1 :
                check = False
    if check :
        print(time)
        break
    
    # after 1,000 sec
    if time >= 1000:
        print(-1)
        break


