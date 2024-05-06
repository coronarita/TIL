def solution(n, k):
    trans = ""
    # n -> k 진수로 변환
    while n: 
        trans = str(n%k) + trans
        n = n//k        
    # print(trans)

    #split with zero
    trans = trans.split("0")

    count = 0
    for t in trans : 
        if len(t)==0: # if empty
            continue
        if int(t)<2 : # if 0 or 1 
            continue
        # Prime Number find 
        sosu=True
        for i in range(2,int(int(t)**0.5)+1) : # 소수 찾기 : 제곱근 까지의 범위
            if int(t)%i==0 :
                sosu=False
                break
        if sosu:
            count+=1      

    return count