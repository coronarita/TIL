n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

    # print(board)

    # chess check => i+j is odd or not
    #   0123
    # 0 WBWB
    # 1 BWBW

    #   0123
    # 0 BWBW
    # 1 WBWB

result = []

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
        for a in range(i, 8+i):
            for b in range(j, 8+j):
                if (a+b) % 2 == 0: # WBWB
                    if board[a][b] == 'B':
                        draw1+=1
                    else : 
                        draw2+=1
                else : # BWBW
                    if board[a][b] == 'W':
                        draw1+=1
                    else : 
                        draw2+=1
        result.append(min(draw1,draw2))

print(min(result))
