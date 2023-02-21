'''
2 4
7 3 1 8
3 3 3 4
'''

n, m = map(int, input().split())
res = []
for i in range(n):
    res.append(sorted(list(map(int, input().split())))[0])
    
print(max(res))