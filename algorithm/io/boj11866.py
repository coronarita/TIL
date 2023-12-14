from collections import deque
n, k = map(int, input().split())

circle = deque([i for i in range(1, n+1)])
answer = []
# [1,2,3,4,5,6,7]
# popleft()-append()를 반복 (k-1회)
# [2,3,4,5,6,7,1]
# [3,4,5,6,7,1,2]
# popleft() (k번째 회)
# [4,5,6,7,1,2]

while len(circle)!= 0:
    # k 번째 사람을 제거
    for i in range(1, k+1):
        if i != k:
            temp = circle.popleft()
            circle.append(temp)
        else :
            temp = circle.popleft()
            answer.append(temp)
print('<', end='')
for i in range(len(answer)):
    if i <len(answer)-1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end='')
print('>')

