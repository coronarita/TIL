'''
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
'''
# python 3 시간초과 문제 -> import sys / input = sys.stdin.readline 사용 시 해결 가능 !
# 참고 : https://breakcoding.tistory.com/109
'''

sys.stdin.readline 적용 시, PyPy3 기준으로 
4892ms --> 252ms 로 많이 감소하는 경향을
확인할 수 있었음 !
'''
import sys
input = sys.stdin.readline

N, M = (map(int, input().split()))
num_list = list(map(int, input().split()))

# 'int' object is not callable -> sum, max 등 예약어를 변수명으로 사용 시 발생
tmp = 0
# sum_list
sum_list = [0]
for n in num_list:
    tmp = tmp + n
    sum_list.append(tmp)
    # print(n)
    # print(sum_list)

for _ in range(M):
    
    i, j = (map(int, input().split()))
    # 3번째 합(12) - 0번째 합(5) = 9
    # j-1          - i-1
    # problem 
    print(sum_list[j]-sum_list[i-1])
        
    
    