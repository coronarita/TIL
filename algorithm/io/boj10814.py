N = int(input())
customer_list = []

for _ in range(N):
    age, name = input().split()
    customer_list.append((int(age), name))  # 숫자는 정렬 시 int 형태로 해줘야 함    

# customer_list.sort(key=lambda x: (x[0], x[1]))
customer_list.sort(key=lambda x: x[0])

for n in range(N):
    print(*(customer_list[n]))

