# input n, m
n, m = map(int, input().split())

# map info
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs
def dfs(x, y):
    # coverage
    if 0 <= x < n and 0<= y < m :
        # not visited
        if graph[x][y] == 0 :
            graph[x][y] = 1
            # recursively call dfs for 4 directions
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
            
    
    else :
        return False


# for all node, fill drink
result = 0
for i in range(n):
    for j in range(m):
        # with dfs
        if dfs(i,j) == True : 
            result += 1
            
print(result)