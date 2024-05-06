# 최소로 거슬러 줄 동전의 갯수

n = 1260

count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(coin)