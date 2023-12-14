# 큰수의 법칙
'''
주어진 수들을 M번 더하여 가장 큰 수를 만들기
특정 인덱스의 수가 연속해서 K번 더해질 수 없음.
2,4,5,4,6 - m=8,k=3
6+6+6+5+6+6+6+5 = 46
서로 다른 인덱스 - 서로 다른 것임
3,4,3,4,3 - m=7, k=2
2,4,2,4,2,4 => 4+4+4+4+4+4+4 = 28
'''

n, m, k = map(int, input().split())
# print(n,m,k)
num_list = list(map(int, input().split()))
# print(num_list)
num_list.sort()
first = num_list[n-1]  # 6
second = num_list[n-2]  # 5
# print(first, second)

# 일반식을 찾는게 중요! 

count = int(m / (k+1)) * k
count += m%(k+1)

result = 0 
result += (count) * first
result += (m-count) * second

print(result)
# m번 더해, 같은 수 k번 이상 불가능
# j = 0
# for i in range(m):
    
#     if count < k :
#         answer += num_list[j]
#         count +=1
#     else :
#         count = 0
#         j += 1
#         answer += num_list[j]
#         j = 0
#     print(count, answer)