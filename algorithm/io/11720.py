import sys

n = int(sys.stdin.readline())
n_list = sys.stdin.readline()
ans = 0

for a in n_list:
    ans += int(a)
    
print(ans)