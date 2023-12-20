import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else :
            absol , origin = heapq.heappop(heap)
            print(origin)
    else :
        heapq.heappush(heap, (abs(x), x))