def solution(survey, choices):
    answer = ''
    # 1. hash 로, 공간 생성 
    res = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0, }

    # 2. choices -> -3 ~ 3으로 변환
    for idx, c in enumerate(choices) : 
        c = c - 4
        choices[idx] = c

    # 3. 각 경우에 맞게 res 값 업데이트
    for i in range(len(survey)) :
        if choices[i] < 0 :
            res[survey[i][0]] += abs(choices[i])
        elif choices[i] > 0 :
            res[survey[i][1]] += (choices[i])

    # 4. 결과 판별
    if res['R'] >= res['T'] : answer += 'R'
    else : answer += 'T'
    if res['C'] >= res['F'] : answer += 'C'
    else : answer += 'F'
    if res['J'] >= res['M'] : answer += 'J'
    else : answer += 'M'
    if res['A'] >= res['N'] : answer += 'A'
    else : answer += 'N'


    return answer
