n = int(input())

stack = []

for _ in range(n):
    a = list(input().split())
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if len(stack) :
            print(stack.pop())
        else : 
            print(-1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) :
            print(0)
        else : 
            print(1)
    elif a[0] == 'top':
        if len(stack) :
            print(stack[-1])
        else : 
            print(-1)

    
    
