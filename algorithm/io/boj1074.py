# z 모양 구성하는 4방향에 대해 차례대로 재귀적으로 호출
# 구현이 어렵고 실수가능성 있음

def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result +=1
        if x == X and y + 1== Y:
            print(result)
            return
        result +=1

        if x + 1 == X and y == Y:
            print(result)
            return
        result +=1

        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result +=1
        return
    solve(n / 2 , x, y)
    solve(n / 2 , x, y+ n/2)
    solve(n / 2 , x+n/2, y)
    solve(n / 2 , x+n/2, y+n/2)




result = 0
N, X, Y = map(int, input().split(' '))
solve(2**N, 0, 0)

