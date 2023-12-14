import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면
    if parent[x] != x:
        # 루트 찾을 때 까지 재귀적 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 찾기
# 점 : 해당 플레이어가 선택한 두 점 !!! - 간선을 만들었으니까, 유니언 성립 되는 거지

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]
# print(parent)

cycle = False

for i in range(m): # m 은 합치기 전 연산의 수와 동일
    a, b = map(int, input().strip().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle= True
        print(i+1)
        break
    else:
        union_parent(parent, a, b)

if not cycle :
    print(0)