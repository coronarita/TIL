import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 연결요소의 개수를 세기
# 합친 다음 개수를 세면 됨

def find_parent(parent, x): # recursively find parent
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 부모테이블 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(m): # m 은 합치기 연산의 수와 동일
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# count the set
counter = set()
for i in range(1, n+1):
    counter.add(find_parent(parent, i))

# print the result
print(len(counter))