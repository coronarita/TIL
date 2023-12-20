import re

def solution(s):
    if len(s) <= 2:
        return len(s)
    
    resultCount = []
    #1. only half length be searched
    for i in range(1, len(s)//2 + 1):
    # 2. make list using regex(sub : regex, replacement, target)
        reList = re.sub('(\w{%i})' %i, '\g<1> ' , s).split() # choose i word then make group 
        # print(i, reList)
        count = 1
        result = []
        
        # 3. Scan 
        for j in range(len(reList)):
            if j < len(reList)-1 and reList[j] == reList[j+1]:
                count += 1
                # print(reList[j], reList[j+1])
            # 4. if catching repeated word
            else :
                if count == 1:
                    result.append(reList[j])
                    # print(reList[j])
                else : 
                    result.append(str(count) + reList[j])
                    count = 1
                    # print(result)
        # print(result)
        # 5. save the result
        resultCount.append(len(''.join(result)))
        # print(resultCount)
    # 6. pick the minimum number
    return min(resultCount)
        
        # return resultCount