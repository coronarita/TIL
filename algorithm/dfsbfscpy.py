from collections import deque

#dfs : with stack(LIFO)
# with recursive
#bfs : with queue(FIFO)
# with deque

def dfs(v):
	print(v, end=" ")
	visited[v] = True

	for e in adj[v]:
		if not(visited[e]):
			dfs(e)


def bfs(v):
	q = deque([v])

	while q:
		v = q.popleft()
		if not(visited[v]):
			print(v, end=" ")
			visited[v] = True

			for e in adj[v]:
				if not(visited[e]):
					q.append(e)



n, m, v = map(int, input().split())

adj = [[] for _ in range(n+1)]

# input adj

for _ in range(m):
	x, y = map(int, input().split())
	adj[x].append(y)
	adj[y].append(x)

for e in adj:
	e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)


