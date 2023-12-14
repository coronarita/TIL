N = int(input())
n_list = list(map(int, input().split()))
v = int(input())


cnt = 0

for n in n_list:
    if v == n : 
        cnt+= 1
        
print(cnt)