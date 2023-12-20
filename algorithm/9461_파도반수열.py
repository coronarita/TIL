dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for n in range(6, 101):
    dp[n] = dp[n-2] + dp[n-3]

T = int(input())
for i in range(0,T):
    print(dp[int(input())])