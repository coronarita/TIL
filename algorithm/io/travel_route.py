# travel route programmers lv.3 
# principle : using DFS

# variable
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    # 시작점의 인접리스트 산출
    for key, val in tickets : 
        graph[key].append(val)
    # print(graph)
    # 도착점 기준 알파벳순 정렬
    for g in graph:
        graph[g].sort()

    def dfs(graph):
        answer = [] # 경로
        stacks = ["ICN"] # 스택

        while stacks :
            stack = stacks[-1]
            # 시작점에 없거나, 더 이상 갈 곳이 없음
            if stack not in graph or len(graph[stack]) == 0 :
                answer.append(stacks.pop())
            else : # 경로에 stack 추가
                stacks.append(graph[stack].pop(0))

        return answer[::-1]

    answer = dfs(graph)
    return answer


# def solution(tickets):
#     # 초기화
#     answer = ["ICN"]
#     remained_list = [] # 임시 보관
    
#     # 함수 호출 시마다, 시작 공항, 남은 경로 리스트를 전달 / 반복
#     def dfs_search(start, tickets):
#         if not tickets:
#             return
#         # 선택 공항, 인덱스(공항 제거를 위함)를 같이 저장
#         temp_list = {}
#         for idx, ticket in enumerate(tickets):
#             if ticket[0] == start :
#                 temp_list[ticket[1]] = idx
#                 print(temp_list)
#         # 만일 start에서 갈 수 있는 공항을 찾지 못하면
#         if len(temp_list) == 0:
#             remained_list.append(answer.pop())
#             dfs_search(answer(-1), tickets)
#         else :  # 목적지 정렬, 알파벳 순으로 높은것 뽑기 위해  
#             temp_list = sorted(temp_list.items(), key = lambda item:item[0])
            
#             ticket = temp_list[0][0]
#             answer.append(ticket)
#             i = temp_list[0][1]
#             del tickets[i]
#             dfs_search(ticket, tickets)
#     dfs_search("ICN", tickets)
#     if len(remained_list) > 0:
#         while remained_list :
#             answer.append(remained_list.pop())
#     return answer
print(solution(tickets))