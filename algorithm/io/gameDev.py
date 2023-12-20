'''
이코테 p118

input
'''
# Direction
# dn = [0, 1, 2, 3] # U, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

class player():
    def __init__(self) -> None:
        # input the data
        self.n, self.m = map(int, input().split())
        self.y, self.x, self.dir = map(int, input().split())
        # self.x = x
        # self.y = y
        # self.dir = dir
        self.visited = [] # 방문정보를 저장하기 위해
        self.map_info = [] # 맵 정보를 그리기 - 육지 : 0, 바다 : 1
        self.count = 0
        self.turn_time = 0
        
    def drawMap(self):        
        for _ in range(self.n):
            self.map_info.append(list(map(int, input().split())))
            
        self.visited = [[0] * self.m for _ in range(self.n)]
        self.visited[self.x][self.y] = 1 # starting point
        self.count = 1
                
    def turn(self): # *** 조금만 쉽게 생각하자..
        # turn ccw : 0 --> 3
        self.dir -= 1
        if self.dir == -1 : 
            self.dir = 3
        
    def move(self):
        while True : 
            self.turn()
            nx = self.x + dx[self.dir]
            ny = self.y + dy[self.dir]
            
            # 맵 밖으로 나가지 못함, 제한조건이 있어서 (가장자리가 바다)
            if self.visited[nx][ny] == 0 and self.map_info[nx][ny] == 0 : 
                self.visited[nx][ny] = 1
                self.x = nx
                self.y = ny
                self.count += 1
                self.turn_time = 0
                continue
                
            else : 
                self.turn_time += 1
            
            if self.turn_time == 4 : 
                nx = self.x - dx[self.dir]
                ny = self.y - dy[self.dir]
                
                if self.map_info[nx][ny] == 0 :
                    self.x = nx
                    self.y = ny
                    
                else : 
                    break
                self.turn_time = 0 
        
        

        
        
# # input the data
# n, m = map(int, input().split())
# pos_y, pos_x, dir = map(int, input().split())

a = player()
a.drawMap()
a.move()
print(a.count)