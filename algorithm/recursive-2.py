def func(n):
    '''
    정수 n에 대해 n이 홀수이면 3 X n + 1을 하고
    n이 짝수이면 n을 2로 나눕니다.
    
    n일 1이 될때까지 반복
    '''
    print(n)
    if n == 1:
        return n
    
    if n % 2 == 0:
        return func(n // 2)
    else :
        return func(3 * n + 1)
    
a = int(input())
print(func(a))
