# input : size of grid, number of player, number of game turn
n, m, k = map(int, input().split())

# Direction : U R D L
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# gun info : 2D-array - n if gun exist, 0 if nothing 
# - list for pick and drop (오답노트, 내가 생각하지 못한 포인트임)
gun = [[[] for i in range(n)] for i in range(n)]

for _ in range(n):
    gun.append(list(map(int, input().split())))
print(gun)
player = []
# player info : posX, posY, Direction, ability
for _ in range(m):
    player.append(list(map(int, input().split())))

# point
points = [0] * m
'''
# OOP for game procedure
# class Game:
#   def __init__(self, player, gun):
#     self.player = player
#     self.gun = gun

# a = Game(player, gun)
# print(a.player)
# print(a.gun)

'''


def move_player(i):
    direction = player[i][2]
    nx = player[i][0] + dx[direction]
    ny = player[i][1] + dy[direction]
    # outside of grid
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        direction = (direction + 2) % 4
        nx = player[i][0] + dx[direction]
        ny = player[i][1] + dy[direction]
    # change position
    player[i][0], player[i][1] = nx, ny


def check_map(i):
    # match with other players - 다른 플레이어 간 비교를 어떻게..?
    # for j in range()
    return True

    return False


def pick_gun():
    pass


def drop_gun():
    pass


def fight():
    pass


def calculate_score():
    pass


# Game start for k-turns
# for _ in range(k):
#   for i in range(m) : # i : player number
#     move_player(i)
#     if check_map(i) : # 플레이어가 있으면

#     else : # 플레이어가 없으면
