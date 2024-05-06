import sys
input = sys.stdin.readline
N = int(input())

import heapq

heap = []
cnt = 0
dasom = int(input())

for _ in range(N-1):
    x = int(input())
    if x >= dasom:
        heapq.heappush(heap, -x)

while heap:
    t = -heapq.heappop(heap)
    if dasom > t :
        break
    cnt +=1 
    dasom += 1
    heapq.heappush(heap, -(t-1))


print(cnt)