
n = int(input())
get_money = list(map(int,input().split()))
# print(get_money)

# 시간을 최소화하기 위하여 정렬
get_money.sort()
# 누적합 어레이
s = [sum(get_money[:i+1]) for i in range(n)]
print(sum(s))