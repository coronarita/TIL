# 숫자카드게임
'''
가장 높은 숫자 한 장을 뽑는 것

N X M 의 형태로 놓여있다. (행, 열의 개수)
행 선택 - 그 행에서 가장 낮은 카드 뽑기
최종적으로 가장 높은 숫자의 카드

'''

# 입력받기
n, m = map(int, input().split())
card = []
for i in range(n):
    card.append(list(map(int, input().split())))
 
ans = -1e9

for i in range(n):
    # print(min(card[i]))
    ans = max(ans, min(card[i]))
    
print(ans)