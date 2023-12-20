a,b,c = map(int, input().split())
import collections
result = collections.defaultdict(list)

# a+b+c 의 갯수를 카운트해서 max값을 return 하면 되지 않을까 
# 20*40*40 <<<10^9 o(n^3)이지만 수가 작아서

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            total = i+j+k
            result[total].append(i+j+k)

print(max(result, key = lambda x : len(result[x])))