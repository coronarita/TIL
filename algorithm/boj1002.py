'''
조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.

이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
'''
import math
import sys
input = sys.stdin.readline


T = int(input())
ans = 0

for _ in range(T):
    # input coordinates
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2) 
    # calculate the number of available position.
    # case 1 : same centroid    
    if d == 0 and r1 == r2 : # with same radius
        ans = -1
    # case 2 : inscribed or circumscribed (meet at 1 point)
    elif abs(r1-r2) == d or r1+r2 == d : 
        ans = 1
    # case 3 : meet at 2 diff points 
    elif abs(r1-r2) < d < r1+r2 :
        ans = 2
    else : 
        ans = 0
    
    print(ans)