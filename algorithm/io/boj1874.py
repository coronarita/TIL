import sys

input = sys.stdin.readline

n = int(input())

stack = []
answer = []
current = 1

for _ in range(n):
    a = int(input().strip())

    while len(stack) == 0 or stack[-1] < a:
        stack.append(current)
        current +=1 
        answer.append('+')
    
    if stack[-1] == a:
        stack.pop()
        answer.append('-')
    else:
        answer = ['No']
        break

for x in answer : 
    print(x)