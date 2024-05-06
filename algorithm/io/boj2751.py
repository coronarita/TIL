# 병합정렬(Merge sort) 알고리즘 - 재귀함수와 분할정복(divide & conquer)
# 절반씩 합치면서 정렬시, 전체 리스트가 정렬 됨
# 시간복잡도 - o(nlogn)

def merge_sort(array):
    if len(array) <= 1 :
        return array  # exception (할게 없다.)
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i,j,k = 0, 0, 0

    while i < len(left) and j < len(right): # 각각 정렬을 진행
        if left[i] < right[j] :
            array[k] = left[i]
            i += 1
        else : 
            array[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i< len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)


'''
submitted answer (first)

import sys
input = sys.stdin.readline
# time complexity : n = 10**6, nlogn 의 시간복잡도를 가져야 한다.
N = int(input())
n_list =[]

for _ in range(N):
    n_list.append(int(input().strip()))

n_list.sort()


for i in range(N):
    print(n_list[i])


'''