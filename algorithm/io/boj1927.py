import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input().strip())
    if x == 0 :
        if len(heap) > 0 :
            print(heapq.heappop(heap))
        else : 
            print(0)
    else : 
        heapq.heappush(heap, x)
