def solution(phone_book):
    
    # 서로 탐색 (포함되면) false
    # 접두어가 되기위해 - length 순으로 정렬 필요
    phone_book.sort()
    #    
    for i in range(len(phone_book)-1): 
        if phone_book[i] == (phone_book[i+1])[:len(phone_book[i])] : 
            return False
    return True
    return answer

