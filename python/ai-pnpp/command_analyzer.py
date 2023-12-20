import csv

def getKey(item):           # 정렬을 위한 함수
    return item[1]          # 신경 쓸 필요 없음

command_data = []           # 파일 읽어오기
with open('data.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)
# print(command_data)         # 모른다고 가정하고, 데이터값 확인해보기
        
command_counter = {}        #dict 생성, id: key, 입력줄: val
for data in command_data:   # list 를 dict로 변환
    if data[1] in command_counter.keys(): # 아이디가 이미 key값으로 변경되었을 때 
        command_counter[data[1]] += 1       # 기존 출현한 아이디
    else :
        command_counter[data[1]] = 1        # 처음 나온 아이디
        
# print(command_counter)
        
dictlist = []                               # dict를 리스트로 변경
for k, v in command_counter.items():
    temp = [k, v]
    dictlist.append(temp)

# print(dictlist)

sorted_dict = sorted(dictlist, key=getKey, reverse=True) # list를 입력 줄 수로 정렬
# getKey : 1번째(숫자값) 기준으로 정렬
print(sorted_dict[:100])                                # list의 상위 100개값 출력

