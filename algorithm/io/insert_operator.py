N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxi = -1e9
mini = 1e9

def dfs(depth, total, plus, minus, multip, divi):
    global maxi, mini
    if depth == N :
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    if plus:
        dfs(depth+1, total + num[depth], plus-1, minus, multip, divi)

    if minus:
        dfs(depth+1, total - num[depth], plus, minus-1, multip, divi)

    if multip:
        dfs(depth+1, total * num[depth], plus, minus, multip-1, divi)

    if divi:
        dfs(depth+1, int(total / num[depth]), plus, minus, multip, divi-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)
