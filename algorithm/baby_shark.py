'''
삼성전자 2020 기출

N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

테케 
---

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

답
14
'''


from collections import deque
INF = 1e9 # infinity

# mapsize
n = int(input())



# whole map information
array = []
for i in range(n):
	array.append(list(map(int,input().split())))

# 현재 크기, 위치
now_size = 2
now_x, now_y = 0, 0

# 아기상어의 시작 위치 찾은 후, 그 위치에 아무것도 없다고 처리
for i in range(n):
	for j in range(n):
		if array[i][j] == 9:
			now_x, now_y = i, j
			array[now_x][now_y] = 0 # 상어의 위치이지, 먹이는 없으니까

# 방향정의(UDLR)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단거리 계산 - 'BFS'
def bfs():
	# 값이 -1 이라면, 도달 불가능  (초기화)
	dist = [[-1]*n for _ in range(n)]
	# 시작위치 - 도달 가능, 거리 0
	q = deque([(now_x, now_y)])
	dist[now_x][now_y] = 0
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0<= ny < n :
				# 물고기의 크기가 작거나 같은 경우 지나갈 수 있음
				if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
					dist[nx][ny] = dist[x][y] + 1
					q.append((nx,ny))
	# 모든 위치까지의 최단거리 테이블 반환
	return dist


# 물고기 탐색 함수 - 최단거리 테이블이 주어졌을 때, 먹을 물고기를 탐색
def find(dist):
	x,y = 0, 0
	min_dist = INF # 
	for i in range(n):
		for j in range(n):
			# 도달 가능, 먹을 수 있는 물고기
			if dist[i][j] != -1 and 1<= array[i][j] <now_size:
				# 가장 가까운 물고기 1마리 선택
				if dist[i][j] <min_dist:
					x, y = i, j
					min_dist = dist[i][j]
	if min_dist == INF: # 먹을 물고기가 없다
		return None
	else :
		return x, y, min_dist # 먹을 물고기 위치와 최단거리

result = 0 # 최종 답
ate = 0 # 현재 크기에서 먹은 양

while True:
	# 먹을 수 있는 물고기 위치 찾기
	value = find(bfs())

	# 먹을 수 있는 물고기 없는 경우, 현재까지 움직인 거리 출력
	if value == None : 
		print(result)
		break
	else:
	# 현재 위치갱신 및 이동거리 변경
		now_x, now_y = value[0], value[1]
		result += value[2]

	# 먹은 위치에는 아무것도 없도록 처리
	array[now_x][now_y] = 0
	ate += 1

	# 이상으로 먹은 경우, 크기 증가
	if ate >= now_size:
		now_size += 1
		ate = 0