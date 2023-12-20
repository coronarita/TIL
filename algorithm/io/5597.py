import sys
data = []
for _ in range(28):
    data.append(int(sys.stdin.readline()))

data.sort()
# print(data)
comp = list(range(1,31))
# print(comp)

# ** 리스트간 차집합 계산 시 리스트컴프리헨션을 활용!! 
sub_set = [x for x in comp if x not in data]
# print(sub_set)

print(sub_set[0])
print(sub_set[1])