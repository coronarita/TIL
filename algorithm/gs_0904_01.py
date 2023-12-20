def solution(nums):  
    answer = len(nums)/2
    
    
    temp = len(set(nums))
    if temp < answer :
        answer = temp
        
    print(answer)
    return answer

#   다른사람의 풀이 : 매우 간결했음.
#   def solution(ls):
#   return min(len(ls)/2, len(set(ls)))
