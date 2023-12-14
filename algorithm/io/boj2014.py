import heapq
import sys
input = sys.stdin.readline

K, N = map(int, input().split())

sosu = list(map(int, input().split()))

# 1. 최소 힙 - 모든 소수 삽입
# 2. top() 꺼내서
# 3. 처음의 소수들과 곱한 결과를 다시 삽입
# 4. 힙의 크기가 N 이상, 힙의 최댓값보다 곱한 결과가 크면 무시
# 한번 구한 결과는 큐에 넣을 필요가 없다.

heap = []
visited = set()  # 이미 처리된 수
max_value = max(sosu)

for x in sosu : # 초기 원소를 최소힙에 삽입
    heapq.heappush(heap, x)

# N - 1 개의 원소 꺼내기
for i in range(N-1): # 힙에서 N-1번 반복해서 원소를 꺼내준다.
    element = heapq.heappop(heap)
    for x in sosu :
        now = element * x # 곱한 결과 계산
        # 힙의 크기가 N 이상이고, 힙의 최댓값보다 곱한 결과가 크다면
        if len(heap) >= N and max_value < now :
            continue
        if now not in visited : # 처음 방문하는 수라면
            heapq.heappush(heap, now)
            max_value = max(max_value, now) # 최댓값 갱신
            visited.add(now) # 방문처리



# N 번쨰 원소 꺼내기
print(heapq.heappop(heap))
