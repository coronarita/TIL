num = input()
# 이중포문 불가
num_list = []
for idx, val in enumerate(num):
    num_list.append(val)
num_list.sort(reverse=True)
for i in range(len(num)):
    print(num_list[i], end="")