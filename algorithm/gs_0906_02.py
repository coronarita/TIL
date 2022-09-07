def hanoi(ans, n, start, end, via):
    if n == 1 :
        ans.append([start, end]) 
        return

    hanoi(ans, n-1, start, via, end)
    ans.append([start, end])
    hanoi(ans, n-1, via, end, start)


def solution(n):
    ans = []
    hanoi(ans, n, 1, 3, 2)

    print(ans)

    return ans
