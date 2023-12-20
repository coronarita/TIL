'''
1이 될때 까지
N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행
N이 K로 나누어떨어질 때 두번째 연산가능
1. n-1
2. n/k

n=17, k=4
최소횟수는 ?
'''

n, k = map(int, input().split())
# print(n,k)

cnt = 0

while n != 1:
    if n%k == 0:
        n/=k
        cnt+=1
    else :
        n -= 1
        cnt+=1
        
print(cnt)