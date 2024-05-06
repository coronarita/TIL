# matrix addition
import sys

N, M = map(int,sys.stdin.readline().split())
A_matrix = []
B_matrix = []

for n in range(N):
    A_matrix.append(list(map(int, sys.stdin.readline().split())))
    
for n in range(N):
    B_matrix.append(list(map(int, sys.stdin.readline().split())))
    
# print(A_matrix, B_matrix)

# list comprehension
# print(B_matrix[N-1][M-1])

S_matrix = [[A_matrix[i][j]+B_matrix[i][j] for j in range(M)] for i in range(N)]

for s in S_matrix:
    print(*s)