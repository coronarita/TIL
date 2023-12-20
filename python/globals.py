def solution(a, b):
    answer = 0
    
    for i in range(a):
        globals()["s{}".format(i)] = i
    print(globals())
    return answer