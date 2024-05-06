'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 
사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는
 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서,
 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
  당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의
   최소 개수를 구하는 프로그램을 작성하시오.
'''

# 필수 알고리즘 : 각 칸의 상하좌우 비교 후 조건에 맞게 변경, 숫자 카운팅 진행
# 첫칸이 흰색,검은색일 경우 고려


# 1. 입력 받기
N, M = map(int, input().split()) # N : 세로/행, M : 가로/열
total_board = []
for _ in range(N):
    total_board.append(input())  # 줄 단위로 입력받기
# print(total_board)
min1 = 99999
min2 = 99999
# 2. 8x8의 사이즈로 체스판 샘플링
for n in range(N-7):
    for m in range(M-7): # n, m은 보드판 샘플링의 시작점 임
        draw1 = 0   # : BWBWBWBW 검출
        draw2 = 0   # : WBWBWBWB 검출

        for i in range(n,n+8):
            for j in range(m,m+8):
                # print(total_board[i][j], i, j)
                # i+j 값의 홀짝여부에 따라 색이 달라짐 (규칙성, 그림그려보면 직관적으로 이해 가능)
                if (i+j)%2 == 0 :  # 시작 기준 B/W 체크
                    if total_board[i][j] == 'W':  # W
                        draw1 += 1
                    else :  # :                     B
                        draw2 += 1                       
                else :  # 시작 다음칸 기준으로 B/W
                    if total_board[i][j] == 'B':  # B
                        draw1 += 1
                    else :  # :                     W
                        draw2 += 1
        min1 = min(min1, draw1) 
        min2 = min(min2, draw2)
        # print(min1,min2)
# 3. 최소값 반환
print(min(min1,min2))