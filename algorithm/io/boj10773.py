import sys
input = sys.stdin.readline

n = int(input())
money =[]
for _ in range(n):
    n = int(input().strip())
    if n :
        money.append(n)
    else : # n == 0
        money.pop()
print(sum(money))