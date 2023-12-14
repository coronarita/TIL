from collections import defaultdict

class Component():
    def __init__(self, t1, t2):
        self.visited = set()  # 방문한 노드들을 저장 (중복 방지)
        self.edges = [[t1[i], t2[i]] for i in range(len(t1))]  # 예 : [[a,b], [b,c], [d,e] ...]로 연결정보를 리스트 쌍의 형태로 만듦
        self.graph = []
        self.components = []

    def make_graph(self):  # edge를 토대로 그래프의 형태로 만듬. {a: {b, c}, b: {a, b, d} ...}
        graph = defaultdict(set)  # 분기문으로 초기화를 하지 않기 위함
        for u, v in self.edges :
            graph[u].add(v) # 그래프의 각 components들은 set의 자료형이기 때문에, add를 사용하여 요소를 추가할 수 있음.
            graph[v].add(u)
        self.graph = graph
            
    def dfs_component(self, node):  # 노드에서 연결된 노드를 찾고, 그 연결된 노드에서 다시 연결된 노드를 찾는다.
        nodes = set([node])
        connected_node = []  # 첫번째 노드로부터 연결된 노드들은 모두 여기에 추가
        while nodes :
            print(nodes)
            node = nodes.pop()  #  연결된 노드에서 뽑고 (여러개 - 작은거 부터 빠짐)
            self.visited.add(node)  # visited에 추가해서 재방문 방지
            connected_node.append(node)  # connected_node에 추가
            # 뽑은 해당 노드와 연결된 노드에서 이미 방문한 노드 제외, 거기서 다시 연결된 노드마다 방문 시작
            nodes |= self.graph[node] - self.visited  #  현재 노드에서 중복/방문된 노드를 제외한 것을 더한다. (dfs)
        return connected_node  # 연결된 쌍을 리스트의 형태로 반환

    def get_connected_components(self):  # graph 내 키 값에 대해 차례대로 검사
        for node in self.graph: # 딕셔너리 형태로 돌릴 경우, 키값이 차례대로 할당 됨
            if node not in self.visited:  # 중복검사 하지않기 위해서
                self.components.append(self.dfs_component(node))
        return self.components

class Group():
    def __init__(self, n):
        self.groups = []  # groups
        self.remains = {*range(1, n+1)}  # 남은 학생들 (그룹이 생기면 여기서 삭제할 것)
        self.reps = []  # 대표들

    def assign(self, t1, t2):
        case = Component(t1, t2)
        case.make_graph()
        self.groups = case.get_connected_components()

    def filter_remains(self, group):  # 혼자잇는 학생들 : 대표
        self.remains = self.remains - group

    def find_reps(self, group):
        group = list(group)
        print(group)
        group.sort(reverse= True) # 짝수 : 번호가 작은 쪽이기 때문에 / 홀수 : 중간 번호를 뽑기위한 정렬
        self.reps.append(group[int(len(group) / 2)])  # 중간번호가 대표학생으로 뽑힘

    def get_result(self):
        self.reps.extend(list(self.remains))  # 혼자 있는 학생들은 대표, reps에 추가
        self.reps.sort()  # 오른차순 정렬
        return self.reps

def solution(n, t1, t2):
    case = Group(n)
    case.assign(t1, t2) # t1, t2를 토대로 그룹 생성
    for group in case.groups : # 그룹마다
        group = set(group)
        case.find_reps(group)  # 그룹에서 대표 찾기
        case.filter_remains(group)  # 해당 그룹 학생은 남은 학생에서 제외
    return case.get_result()  # 최종 결과 리턴

n = 10
t1 = [9, 4, 4, 4, 7] 
t2 = [2, 10, 7, 6, 3] 
print(solution(n, t1, t2))