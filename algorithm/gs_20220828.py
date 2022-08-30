
def solution(absolutes, signs):   

    answer = 0
    int_sign = []
    for s in signs : 
        if s :
            int_sign.append(1)
        else : 
            int_sign.append(-1)
    
    for i, j in zip(absolutes, int_sign) : 
        answer += i * j 
            
            
    return answer
