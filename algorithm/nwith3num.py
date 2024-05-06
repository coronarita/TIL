def func(n):
    '''
    n을 1,2,3의 합으로 나타낼 수 있는 가지 수를 구하기
    '''
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return func(n-1) + func(n-2) + func(n-3)
    
    
a = int(input())
print(func(a))