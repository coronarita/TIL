
ans = [0]*1000

def fibo(n):
    ans[1] = 1
    ans[2] = 2
    
    if n <= 2:
        return ans[n]
    
    for i in range(3, n+1):
        ans[i] = ans[i-1] + ans[i-2]
    return ans[i] % 10007

n = int(input())

print(fibo(n))
