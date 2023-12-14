board = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]],
         [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]]

class Mine():
    def __init__(self, board):
        self.coord = board
        self.N = len(board)
        
    def check_mine_position(self):
        mine_pos = []
        for x in range(self.N):
            for y in range(self.N):
                if self.coord[x][y] == 1 :
                    mine_pos.append((x,y))
        return mine_pos
        
    def set_bomb(self, mine):
        # 11, 12, 1
        # 9, 3
        # 7, 6, 5
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [1, 1, 1, 0, 0, -1, -1, -1]
        for x, y in mine : 
            if self.coord[x][y] == 1:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # inside the board
                    if 0 <= nx < self.N and 0<= ny <self.N :
                        self.coord[nx][ny] = 1
        
    def check_board(self):
        print(self.coord)
        
    def count_safezone(self):
        count = 0
        for x in range(self.N):
            for y in range(self.N):
                if self.coord[x][y] == 0 :
                    count += 1
        return count


def solution(board):
    a = Mine(board)
    # 지뢰의 좌표 체크
    mine = a.check_mine_position()
    # 지뢰 주변에 지뢰 설치
    a.set_bomb(mine)
    # a.check_board()    
    # 지뢰이 설치되지 않은 좌표의 수 세기
    return a.count_safezone()

res = []

for b in board :
    res.append(solution(b))
    print(res)