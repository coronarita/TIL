# 1. 한정적인 변수조건 -> 완전탐색
# 2. 연산자 리스트와 숫자 리스트를 따로 가져감

import copy

def recursive(array, n):
    # n의 길이를 만족하면 반환
    if len(array) == n:
        operators_list.append(copy.deepcopy(array)) # 복사를 해 줘야 함(array 가변적임, 주소 공유)
        return
    # 아닐 경우, 재귀적으로 모든 경우의 수를 생성
    array.append(' ')
    recursive(array, n) # 재귀적으로 호출
    array.pop()

    array.append('+')
    recursive(array, n) # 재귀적으로 호출
    array.pop()

    array.append('-')
    recursive(array, n) # 재귀적으로 호출
    array.pop()


# 입력 받기
for _ in range(int(input())):
    num = int(input())
    n_list = [i for i in range(1, num+1)]
    operators_list = []
    answer = []  # 0이 되는 케이스를 주워담기

    recursive([], num-1)
    # print(operators_list) 연산자의 조합 체크용 



    # 연산자의 조합 별로 연산식을 세운다.
    for operators in operators_list :
        string = ""
        for i in range(len(operators)):
            string += str(n_list[i]) + operators[i]
        
        string += str(n_list[-1])
        # print(string)

        if eval(string.replace(" ", "")) == 0:  # 0이 되면
            answer.append(string)

    # 0이 되는 모든 경우 출력하기
    for i in range(len(answer)):
        print(answer[i])

    print() # 공백으로 테스트케이스 구분하기
