N = int(input())
Map = [[0 for i in range(N)] for i in range(N)]

def star(n):
    global Map
    # 단위 초기화
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return
    
    a = n // 3
    star(n//3) # recursively draw figure
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1 :
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]
    
        
def print_star():
    for i in range(N):
        for j in range(N) :
            if Map[j][i] == 1 :
                print("*", end="")
            else : 
                print(" ", end="")
        print()        
            
star(N)
print_star()