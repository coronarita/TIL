'''
청소년 상어는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

테케
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

정답
14
'''

n, m, k = map(int, input().split())

# 2d list - all position and direction of sharks

array = []
for i in range(n):
	array.append(list(map(int, input().split())))

# current direction information
directions = list(map(int, input().split()))

# 2d list - for smell of the number of shark, the time left to disappear
smell = [[[0, 0]] * n for _ in range(n)]

# priority information of rotation direction information
priorities = [[] for _ in range(m)]
for i in range(m):
	for j in range(4):
		priorities[i].append(list(map(int, input().split())))

# 4 movable direction at specific position
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# for debug !! -> 알고보니, return 의 위치가 반복문 내에 있어서 답에서 오류가 발생.
def check_array(map):
	print("\n")
	for i in range(len(map)):
		print(*map[i],sep=" ") 

	print("\n")

# update all smell information
def update_smell():
	# check each position step by step,
	for i in range(n):
		for j in range(n):
			# if smell exist, decreasing time by 1 (-1)
			if smell[i][j][1] > 0:
				smell[i][j][1] -= 1
			# set 'k', for smell exist with shark
			if array[i][j] != 0:
				smell[i][j] = [array[i][j], k]

# func - for moving all sharks
def move():
	# initialization for temporary results (move)
	new_array = [[0] * n for _ in range(n)]
	# check each position
	for x in range(n):
		for y in range(n):
			# if shark exists
			if array[x][y] != 0:
				direction = directions[array[x][y] - 1] # direction of current shark
				found = False
				# check the location without smell
				for index in range(4):
					nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
					ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]
					if 0<= nx < n and 0 <= ny < n:
						if smell[nx][ny][1] == 0: # if without smell
							# move the direction of the shark
							directions[array[x][y] -1] = priorities[array[x][y]-1][direction-1][index]
							# if other shark exist, shark with low number leave
							#move shark
							if new_array[nx][ny] == 0:
								new_array[nx][ny] = array[x][y]
							else :
								new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
							found = True
							break # 이런거도 빼먹기 쉬움.
				if found :
					continue
				# if smell exist around the shark, will move to the place with its smell
				for index in range(4):
					nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
					ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]
					if 0<= nx < n and 0 <= ny < n:
						if smell[nx][ny][0] == array[x][y]: # smell itself
							# move the direction of the shark
							directions[array[x][y] -1] = priorities[array[x][y] -1][direction -1][index]
							# move the shark
							new_array[nx][ny] = array[x][y]
							break

	return new_array

time = 0

while True:

	update_smell() # update all of the smell position
	check_array(array)
	check_array(smell)

	new_array = move() # move all sharks
	array = new_array # update map
	time += 1 # increase time

	# check whether 1st shark left
	check = True
	for i in range(n):
		for j in range(n):
			if array[i][j] > 1:
				check = False
	if check : 
		print(time)
		break

	if time>= 1000:
		print(-1)
		break

