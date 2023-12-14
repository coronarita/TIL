# 테스트케이스가 끝날 경우 예외처리로 루프 종료 - try / except

while 1:
    try :
        a, b = map(int, input().split())
        print(a+b)
    
    except EOFError:
        break