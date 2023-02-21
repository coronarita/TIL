n = int(input())

# check whether the number '3' included or not
cnt = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            t = str(h)+ str(m) + str(s)
            if '3' in t :
                cnt += 1
print(cnt)