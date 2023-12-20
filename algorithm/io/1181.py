n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input())
    
n_list = list(set(n_list))
n_list = sorted(n_list)
n_list = sorted(n_list, key=lambda x : len(x))

for a in n_list:
    print(a)
