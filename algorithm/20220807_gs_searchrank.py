from bisect import bisect_left

def solution(info, query):
    # 1. 각각의 케이스 인덱싱 (리스트화 : 4 * 3 * 3 * 3 = 108)
    wmap = {
            '-' : 0, 'cpp' : 1, 'java' : 2, 'python': 3,
			'backend':1, 'frontend':2,
			'junior': 1, 'senior':2,
			'chicken':1, 'pizza':2
    }
    # print(wmap)
    slist = [[] for _ in range(4*3*3*3)] # 공간생성
    # print(slist)
    for string in info: 
        w = string.split() # 분리
        arr = (wmap[w[0]]*3*3*3,
				wmap[w[1]]*3*3,
				wmap[w[2]]*3,
				wmap[w[3]])
        score = int(w[4])
        # print(arr)
        # print(score)
        
		# 2. 비트형태로 부분집합
        for i in range(1 << 4): # 2**4만큼 비트연산
            idx = 0
            for j in range(4):
                if i & (1 << j):
                    idx += arr[j]
                
            slist[idx].append(score)
            # print(idx)
        # print(slist)
        
    for i in range(4*3*3*3):
        slist[i] = sorted(slist[i])
        
    # print(slist)

    #3. 쿼리 처리
    answer = []
    for string in query:
        w = string.split() 
        idx = wmap[w[0]]*3*3*3 + wmap[w[2]]*3*3 + wmap[w[4]]*3 + wmap[w[6]]
        score = int(w[7]) # 100 200 300
#         print(w)
#         print(idx)
#         print(score)
        # bisect_left : score 가 들어갈 수 있는 index 값 반환
        answer.append(len(slist[idx]) - bisect_left(slist[idx], score))
        
    return answer