import sys
input = sys.stdin.readline

N = int(input())
coord_list = []

for n in range(N):
    coordinate = input().strip().split()
    coord_list.append((int(coordinate[0]), int(coordinate[1])))

coord_list.sort(key= lambda x : (x[0], x[1]))
# print(coord_list)

for i in range(N):
    print(*coord_list[i])