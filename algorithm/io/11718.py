import sys
for _ in range(100):
    try :
        print(sys.stdin.readline().rstrip())
    except:
        EOFError
        break