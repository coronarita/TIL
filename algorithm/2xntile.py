def func(n):
    '''
    백준 11726  2xn 타일링
    n <= 1,000
    '''
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func(n-1) + func(n-2)


def func_dp(n):
    cache = [0 for idx in range(n+1)]
    cache[1] = 1
    cache[2] = 2
    
    for idx in range(3, n+1):
        cache[idx] = cache[idx-1] + cache[idx-2]

    return cache[n]
# print(func(6))

print(func_dp(6))