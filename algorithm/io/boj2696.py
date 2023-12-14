import sys
import heapq
input = sys.stdin.readline

T = int(input().strip())

def show_result():
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=" ")
        if (i+1) % 10 == 0:
            print()
    print()

for _ in range(T):
    M = int(input().strip())
    n_list = []
    for _ in range(M//10 + 1):
        n_list.extend(list(map(int, input().strip().split())))
    # print(n_list) # io check
    # 홀수번 째 수를 읽을 때 마다 지금까지 입력받은 값의 중앙값을 출력
    

    # 2개의 힙 사용..
    # 최대 - 중앙 -최소 힙의 구조
    # 중앙값보다 작거나 같은 원소 - 왼쪽의 최대힙
    # 중앙값보다 큰 원소 - 오른쪽의 최소힙
            
    left = [] # max heap
    right = [] # min heap
    median = n_list[0]
    result = [median]
    for i in range(1, M): # 하나씩 체크
        if n_list[i] <= median:
            heapq.heappush(left, -n_list[i]) # 최대 힙이기 때문
        else :
            heapq.heappush(right, n_list[i])
        if i % 2 == 0:
            if len(left) > len(right): # 크면 하나 보내줌
                heapq.heappush(right, median)
                median = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, median)
                median = heapq.heappop(right)
            result.append(median)
    show_result()

