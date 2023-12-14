import heapq
import sys
input = sys.stdin.readline

def pop(heap):
   while len(heap) > 0:
      data, id = heapq.heappop(heap)
      if not deleted[id]:  # 처음 삭제하는 원소일 때 
         deleted[id] = True
         return data
   return None

T = int(input())
for _ in range(T):
   k = int(input())
   max_heap = []
   min_heap = []
   current = 0
   deleted = [False] * (k+1)  # 각 원소의 삭제 여부

   for _ in range(k):
      command = input().split()
      operator, data = command[0], int(command[1])
      if operator == 'D':
         if data == -1 : pop(min_heap)
         elif data == 1 : pop(max_heap)
      elif operator == 'I':
         heapq.heappush(min_heap, (data, current))
         heapq.heappush(max_heap, (-data, current))
         current +=1
   max_value = pop(max_heap)
   if max_value == None : print("EMPTY")
   else:
      # max_value는 min_heap에서도 꺼내짐
      heapq.heappush(min_heap, (-max_value, current)) 
      print(-max_value, pop(min_heap))