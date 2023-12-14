N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

def binary_search(value, start, end):
    if start > end:
        return False
    
    median = (start + end)//2 # 변형이니까, 주의할 것, N_list를 전역변수로 사용하고, start, end를 통제
    
    if value > N_list[median]:
        return binary_search(value, median+1, end)
    
    elif value < N_list[median]:
        return binary_search(value, start, median-1)
    
    else : 
        return True

N_list.sort()
for item in M_list :
    if binary_search(item, 0, N-1) :
        print(1)
    else:
        print(0)