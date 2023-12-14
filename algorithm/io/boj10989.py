import sys
input = sys.stdin.readline

N = int(input())
# 메모리 초과 이슈 --> 계수정렬로 해결

n_list = [0] * 10001 # data 수가 10000개로 최대값임

for i in range(N):
    data = int(input())
    n_list[data] += 1

for i in range(10001):
    if n_list[data] != 0:
        for j in range(n_list[i]):
            print(i)
# n_list = []

# for _ in range(N):
#     n_list.append(int(input().strip()))

# n_list.sort()

# for n in range(N):
#     print(n_list[n])

'''
Counting sort : 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬방법
배열의 크기는 데이터의 범위를 포함할 수 있도록
데이터가 등장한 횟수를 셉니다.
최종적으로 인덱스만큼 값을 출력하면 됩니다.
'''

