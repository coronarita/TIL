'''
정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
(공백으로 구분)
'''

N, X = map(int, input().split())
ans= []
A_list = list(map(int, input().split()))
# print(A_list)

for a in A_list :
    if a < X :
        ans.append(a)

print(*ans)
