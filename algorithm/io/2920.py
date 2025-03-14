'''
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. 
c는 1로, d는 2로, ..., C를 8로 바꾼다.
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
'''

n_list = list(map(int, input().split()))

# 7회 loop
# 차이가 모두 -1 : Ascending
# 차이가 모두 1 : Descending

check = []
for n in range(7):
    check.append(n_list[n+1]-n_list[n])
    
if len(set(check)) == 1:
    if 1 in check : 
        print("ascending")
    else : 
        print("descending")
else : 
    print("mixed")