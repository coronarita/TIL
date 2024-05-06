'''
N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.
'''
import sys

T=3
for _ in range(3):
    n = int(sys.stdin.readline())
    S = 0
    for _ in range(n):
        S += int(sys.stdin.readline())
    
    if S == 0:
        print(0)
    elif S > 0:
        print('+')
    else : 
        print('-')