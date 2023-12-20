pos = input()
pos_h = ord(pos[0]) - 96 # to match pos
pos_v = pos[1]
# print(pos_h,pos_v)
# start at 1 # mov를 튜플로 정의해도 무관
kn_mov_h = [1, 2, 2, 1, -1, -2, -2, -1]
kn_mov_v = [-2, -1, 1, 2, 2, 1, -1, -2]

cnt = 0

for i in range(len(kn_mov_h)):
    n_h = int(pos_h) + kn_mov_h[i]
    n_v = int(pos_v) + kn_mov_v[i]
    
    if 0 < n_h <= 8 and 0 < n_v <= 8 : 
        cnt += 1
        
print(cnt)
