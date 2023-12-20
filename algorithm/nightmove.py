P = input()
x = int(P[1])
# y -> using ASCII
y = int(ord(P[0])) - int(ord('a')) + 1

#steps of knight
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
# two ways to define direction
# 1. using list
# 2. using tuple (x, y)
count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else : 
        count += 1

    
print(count)