def fibo_dp(n):
    cache = [0 for idx in range(n+1)]
    cache[0] = 0
    cache[1] = 1
    
    for idx in range(2, n+1):
        cache[idx] = cache[idx-1] + cache[idx-2]
        
    return cache[n]


print(fibo_dp(10))