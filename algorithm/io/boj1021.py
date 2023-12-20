import sys
input =sys.stdin.readline
n, m = map(int, input().split())

# deque

from collections import deque

n_list = deque([i for i in range(1, n+1)])
cnt = 0
a_list = list(map(int, input().split()))

for i in a_list:

    a = n_list.index(i)

    if a <= len(n_list) // 2 :
        for k in range(a):
            t = n_list.popleft()
            n_list.append(t)
            cnt += 1
    else : 
        for k in range(len(n_list) - a):
            t = n_list.pop()
            n_list.appendleft(t)
            cnt += 1
    n_list.popleft()

print(cnt)