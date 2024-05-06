# DFS, BFS

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''

from collections import deque


def check_array(map):
	for i in range(len(map)):
		print(*map[i],sep=" ") 

def dfs(v): # recursive
	print(v, end=" ")
	visited[v] = True
	for e in adj[v]:
		if not visited[e] :
			dfs(e)

def bfs(v):
	q = deque([v])
	while q:
		v = q.popleft()
		if not visited[v]:
			print(v, end=" ")
			visited[v] = True
			for e in adj[v]:
				if not visited[e]:
					q.append(e)



# input

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
	x, y = map(int, input().split())
	adj[x].append(y)
	adj[y].append(x)

for e in adj :
	e.sort() # lowercase

print(adj)

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)