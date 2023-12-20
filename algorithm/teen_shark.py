'''

아기 상어가 성장해 청소년 상어가 되었다.

4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다. 공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다. 한 칸에는 물고기가 한 마리 존재한다. 각 물고기는 번호와 방향을 가지고 있다. 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다. 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다. 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다. 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.

상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.

테케
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

답
33
'''

import copy

# 4 x 4 size - each fish number, direction table

array = [[None] * 4 for _ in range(4)]

for i in range(4):
	data = list(map(int, input().split()))
	# each line, check 4 fishes one by one
	for j in range(4):
		# each position, save the num, dir
		array[i][j] = [data[j*2], data[j*2+1] -1] # -1 -> 0 ~ 7로 방향접근

# 8 direction def (ccw, 45 rotation start form 12)
dx = [-1,-1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# current_position - to left rotation result
def turn_left(direction):
	return (direction + 1) % 8

result = 0 # final result

# find the fish of specific number, in array
def find_fish(array, index):
	for i in range(4):
		for j in range(4):
			if array[i][j][0] == index : 
				return(i,j)
	return None

# move_all_fishes
def move_all_fishes(array, now_x, now_y):
	# check in low order
	for i in range(1, 17):
		# find position of fish
		position = find_fish(array, i)

		if position != None :
			x, y = position[0], position[1]
			direction = array[x][y][1]
			# check with moving, rotation condition
			for j in range(8):
				nx = x + dx[direction]
				ny = y + dy[direction]
				# if available : move
				if 0 <= nx < 4 and 0 <= ny < 4 :
					if not (nx == now_x and ny == now_y): # 괄호 잘 구별해서 체크해야 함
						array[x][y][1] = direction
						array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
						break
				direction = turn_left(direction)


# return whole positions of fish available to eat
def get_possible_positions(array, now_x, now_y):
	positions = []
	direction = array[now_x][now_y][1]
	# continously moving with current direction
	for i in range(4):
		now_x += dx[direction]
		now_y += dy[direction]
		# check out of range
		if 0 <= now_x < 4 and 0<= now_y < 4 :
			# fish exist
			if array[now_x][now_y][0] != -1 :
				positions.append((now_x,now_y))
	return positions

# DFS, to search whole cases
def dfs(array, now_x, now_y, total):

	global result # outside variable to use in local func
	print(result)
	array = copy.deepcopy(array) # cpoy whole list

	total += array[now_x][now_y][0] # eat fish in now_position
	array[now_x][now_y][0] = -1 # set to -1 (empty)

	move_all_fishes(array, now_x, now_y) # move whole fishes

	# shark turn, find movable position
	positions = get_possible_positions(array, now_x, now_y)

	# exit, when there's no movable position
	if len(positions) == 0:
		result = max(result, total) # save maximum 
		return
	# execute recursively to all movable position
	for next_x, next_y in positions:
		dfs(array, next_x, next_y, total)

# at startpoint(0,0), search whole cases
dfs(array, 0, 0, 0)
# print(result)
