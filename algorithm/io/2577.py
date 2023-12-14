a = int(input())
b = int(input())
c = int(input())
  
check = str(a*b*c)

for i in range(10):
    cnt = 0
    for n in check :
        if str(i) == n:
            cnt += 1
    print(cnt)
    
    