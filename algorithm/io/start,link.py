def cal_diff(team_list: list) -> None:
    pass
    


def dfs(team_list: list) -> None:
    if len(team_list) == N/2:
        print(team_list)
        cal_diff(team_list)
        return None
    
    for i in range(team_list[-1] if team_list else 0, N):
        if team_list and team_list[0] != 0:
            return None
        # if i not in team_list:
        team_list.append(i)
        dfs(team_list)
        team_list.pop()
        
    


N = int(input())

team =[]
for _ in range(N):
    team.append(list(map(int, input().split())))
    # print(team)

ans = []
dfs([])
# print(min(ans))



