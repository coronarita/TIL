from itertools import combinations

def solution(orders, course):
    answer = []
    foodMap = [{} for _ in range(11)]
    maxCnt = [0 for _ in range(11)]
    
    for str in orders:
        # sort
        for num in range(2, len(str) + 1) : 
            for i in combinations(sorted(str), num) :
                key = ''.join(i)
                # print(i, type(i))
                # print(key, type(key)) 
                                
                if key in foodMap[num]:
                    foodMap[num][key] += 1
                    maxCnt[num] = max(maxCnt[num], foodMap[num][key])
                else:
                    foodMap[num][key] = 1
                    
                # print(foodMap, maxCnt)
             
    for num in course : 
        for key, value in foodMap[num].items():
            # print(foodMap[num], type(foodMap[num]))
            # print(key, value)
            if value >= 2 and value == maxCnt[num] :
                answer.append(key) 
    
    print(answer)
    
    return sorted(answer)