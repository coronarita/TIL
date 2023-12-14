import sys
input = sys.stdin.readline

N = int(input())
n_list = []
for _ in range(N):
    n_list.append(int(input()))

n_list.sort()

for i in range(N):
    print(n_list[i])