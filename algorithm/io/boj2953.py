from collections import defaultdict

n = 5 


cook = defaultdict()
for i in range(5):
    cook[i] =  list(map(int, input().split()))

total = []
for i in range(5):
    total.append((i+1, sum(cook[i])))

print(*max(total, key = lambda x : x[1]))