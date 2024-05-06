import sys
input = sys.stdin.readline
import heapq

N = int(input().strip())
lecture_room = 1

lec_table = []
for _ in range(N):
    lec_num, lec_start, lec_end = map(int, input().strip().split())
    # lec_table.append((lec_start, lec_end))
    heapq.heappush(lec_table, (lec_start, lec_end)) # 자동으로 정렬
# print(lec_table)
# 동시에 강의하지 못함    
# 최소강의실 개수 출력
# 정렬
# lec_table.sort(key=lambda x: x[1])
# print(lec_table)

heap = []

end = heapq.heappop(lec_table)[1]
heapq.heappush(heap, end)
# print(heap) # 처음나온 end_time을 넣어줌

for i in range(N-1):
    new_start, new_end = heapq.heappop(lec_table) # input과
    end = heapq.heappop(heap) # 저장해놓은 end time 중 가장 작은게 추출
    if new_start < end :
        heapq.heappush(heap, end)
        heapq.heappush(heap, new_end)
        lecture_room += 1
    else : # new_start > end
        heapq.heappush(heap, new_end)

print(lecture_room)