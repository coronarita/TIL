n = 9
money = [2,3,4]

def solution(n, money):
    dp = [1, *(0 for _ in range(n))]
    for m in money:
        for idx in range(m,n+1):
            dp[idx] = (dp[idx]+dp[idx-m])%1_000_000_007

            print(dp)
    return dp[-1]

print("ans :",solution(n, money))
