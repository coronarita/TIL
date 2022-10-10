# 백준 11047 동전1
n, k = map(int, input().split())

coin = []
count = 0

for i in range(0, n):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(0, n):
    # 동전의 가치가 k보다 작거나 같을 때 인데, 작은 케이스면 생각해서 틀림
    if coin[i] <= k :           
        count += (k // coin[i])
        k %= coin[i]
        
        
print(count)