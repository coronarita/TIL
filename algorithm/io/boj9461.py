ans = [0] * 101

def surf_class(N):
    
    ans[1] = 1
    ans[2] = 1
    ans[3] = 1
    ans[4] = 2
    ans[5] = 2
    
    if N<6 : 
        return ans[N]
    
    for i in range(6,N+1):
        ans[i] = ans[i-1] + ans[i-5]
    return (ans[i])

for _ in range(int(input())) :
    N = int(input())
    print(surf_class(N))
    
    

    