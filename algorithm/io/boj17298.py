import sys
input = sys.stdin.readline
n = int(input())
# 시간 초과 문제에 따라, 재코딩 진행 (답은 구하였음. 시간복잡도 처리 문제)

# 아이디어 : 오큰수를 찾지 못한 수들을 스택에 쌓는다.
stack = []
arr = list(map(int, input().split()))
NGE = [-1] * n

for i in range(n):
    x = arr[i]
    # insert until finding the nearest right top number
    if len(stack) == 0 or stack[-1][0] >= x :
        stack.append((x, i))
    else : # popping reversely
        while len(stack) > 0:
            prev, index = stack.pop()
            if prev >= x: # prev가 더 클 경우 스탑
                stack.append((prev, index))
                break
            else : 
                NGE[index] = x
        stack.append((x, i))

for x in NGE:
    print(x, end = ' ')