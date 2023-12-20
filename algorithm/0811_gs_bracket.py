def solution(p):
    def divide_uv(s):
        count_l = 0
        count_r = 0
        for i in range(len(s)):
            if s[i] == '(':
                count_l += 1
            else : # s[i] == ')'
                count_r += 1
            if count_l == count_r:
                break
        return s[:i+1], s[i+1:]
                
    def right(s): # num of '(' != num of ')' --> until be same
        result = True
        count = 0
        
        for i in range(len(s)):
            if s[i] =='(' : 
                count += 1
            else : # s[i] == ')':
                count -= 1
            if count < 0:
                result = False
                break
        return result
          
    if p == '' : # cond 1
        return ''
    
    u, v = divide_uv(p) # cond 2
    # print(u, v)
    if right(u) : # cond 3
        return u+solution(v) # recursive
    else : # right(u) == False
        answer = '(' # cond 4-1
        answer += solution(v) # cond 4-2
        answer += ')' # cond 4-3
        
        del_u = u[1:-1] # cond 4-4
                
        for i in range(len(del_u)):
            if del_u[i] == '(':
                answer += ')'
            else : # del_u[i] == ')'
                answer += '('
        return answer # cond 4-5