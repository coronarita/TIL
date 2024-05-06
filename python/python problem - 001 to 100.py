#!/usr/bin/env python
# coding: utf-8

# # 001 ~ 010

# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.

# In[2]:


print('Hello World')


# 002 print 기초
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)

# In[3]:


print('Mary\'s cosmetics')


# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 
# 신씨가 소리질렀다. "도둑이야".

# In[4]:


print('신씨가 소리질렀다. "도둑이야".')


# 004 print 기초
# 화면에 "C:\Windows"를 출력하세요.

# In[5]:


print('"C:\\Windows"')


# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
# 
# print("안녕하세요.\n만나서\t\t반갑습니다.")

# In[7]:


print("안녕하세요.\n만나서\t\t반갑습니다.")


# ▶ \n : Enter(개행), \t : Tab(공백)

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
# 
# print ("오늘은", "일요일")

# ▶오늘은 일요일

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# 
# naver;kakao;sk;samsung

# In[10]:


print('naver;kakao;sk;samsung')


# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# 
# naver/kakao/sk/samsung

# In[11]:


print('naver/kakao/sk/samsung')


# ## 009 print 줄바꿈 (end=" ")
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# 
# print("first");print("second")

# In[16]:


print("first", end=" ");print("second") # end=" " print 함수 간 개행 미적용 및 "" 안의 string 적용


# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.

# In[22]:


print(f'{5/3}') # f-string 사용
print(5/3) # string 없이 바로 적용 하면 계산 가능


# # 011 ~ 020

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

# In[23]:


삼성전자 = 50000
평가금액 = 삼성전자 * 10
print(평가금액)


# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 
# 항목	값
# 시가총액	298조
# 현재가	50,000원
# PER	15.79

# In[29]:


시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액)) # type : 변수 타입 출력
print(현재가, type(현재가))
print(PER, type(PER)) 

013 문자열 출력
변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.

>> s = "hello"
>> t = "python"
두 변수를 이용하여 아래와 같이 출력해보세요.

실행 예:
hello! python
# In[31]:


s = "hello"
t = "python"

print(s + "!", t)


# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# 
# >> 2 + 2 * 3 
# 

# In[ ]:


▶ 2 + 6 = 8


# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# 
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# 
# >> a = "132"

# In[33]:


# ▶ string
a = "132"
type(a)


# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.
# 
# >> num_str = "720"

# In[36]:


num_str = "720"
a = int(num_str)
print(a, type(a))


# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
# 
# num = 100
# 

# In[37]:


num = 100
s = str(num)
print(s, type(s))


# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

# In[38]:


n_str = "15.79"
n = float(n_str)
print(n, type(n))


# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
# 
# year = "2020"

# In[39]:


year = "2020"
y = int(year)
print(y, y+1, y+2)


# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

# In[40]:


installment = 48584
month = 36
print(installment * month)


# # 021 ~ 030

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# 
# >> letters = 'python'
# 실행 예
# p t

# In[4]:


letters = 'python'
print(letters[0:3:2])
print(letters[0],letters[2])


# # 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# 
# >> license_plate = "24가 2210"
# 실행 예: 2210

# In[6]:


license_plate = "24가 2210"
print(license_plate[-4:])


# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# 
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

# In[9]:


string = "홀짝홀짝홀짝"
print(string[::2])


# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# 
# >> string = "PYTHON"
# 실행 예:
# NOHTYP

# In[10]:


string = "PYTHON"
print(string[::-1])


# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# 
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

# In[12]:


phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))


# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 
# 실행 예
# 01011112222

# In[13]:


print(phone_number.replace("-",""))


# ## 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# 
# >> url = "http://sharebook.kr"
# 실행 예:
# kr

# In[16]:


url = "http://sharebook.kr"
print(url.split('.'))
print(url.split('.')[1])


# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# 
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

# ▶ python (P로 대체 X, Char 개별로 할당 불가능)

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# 
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A

# In[17]:


string = 'abcdfe2a354a32a'
print(string.replace('a','A'))


# ## 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# 
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

# ▶ abcd (string 자체가 변경되지 않았음)

# # 031 ~ 040

# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
# 
# >> a = "3"
# >> b = "4"
# >> print(a + b)

# In[ ]:


# 34


# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# 
# >> print("Hi" * 3)

# In[ ]:


#HiHiHi


# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
# 
# 실행 예:
# --------------------------------------------------------------------------------

# In[18]:


print('-'*80)


# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# 
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 
# 실행 예:
# python java python java python java python java

# In[30]:


t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ')*4)


# ## 035 문자열 출력 [%d, %사용]
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# 
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

# In[39]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %d'%(name1,age1))
print('이름: %s 나이: %d'%(name2,age2))


# ## 036 문자열 출력 [.format] 사용
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.

# In[40]:


print('이름: {} 나이: {}'.format(name1,age1))
print('이름: {} 나이: {}'.format(name2,age2))


# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.

# In[41]:


print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')


# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 
# 상장주식수 = "5,969,782,550"

# In[43]:


상장주식수 = "5,969,782,550"
a = int(상장주식수.replace(',',''))
print(a)


# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 
# 분기 = "2020/03(E) (IFRS연결)"

# In[45]:


분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])


# ## 040 strip 메서드 [.strip() - 공백 제거 후 새로운 문자열 반환]
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# 
# data = "   삼성전자    "

# In[47]:


data = "   삼성전자    "
print(data.strip())


# # 041 ~ 050

# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# 
# ticker = "btc_krw"

# In[48]:


ticker = "btc_krw"
print(ticker.upper())


# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# 
# ticker = "BTC_KRW"

# In[49]:


ticker = "BTC_KRW"
print(ticker.lower())


# ## 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

# In[51]:


string = 'hello'
# print(string.replace('h','H')
print(string.capitalize())


# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# 
# file_name = "보고서.xlsx"

# In[53]:


file_name = "보고서.xlsx"
file_name.endswith('xlsx')


# ## 045 endswith 메서드 (두가지 조건 - , 로 구분)
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# 
# file_name = "보고서.xlsx"

# In[58]:


file_name = "보고서.xlsx"
file_name.endswith(('xlsx','xls'))


# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
# 
# file_name = "2020_보고서.xlsx"

# In[59]:


file_name = "2020_보고서.xlsx"
file_name.startswith('2020')


# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# 
# a = "hello world"

# In[60]:


a = "hello world"
a.split()


# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# 
# ticker = "btc_krw"

# In[61]:


ticker = "btc_krw"
ticker.split('_')


# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# 
# date = "2020-05-01"

# In[62]:


date = "2020-05-01"
date.split("-")


# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# 
# data = "039490     "

# In[67]:


data = "039490     "
data.rstrip()


# # 051 ~ 060

# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키

# In[70]:


movie_rank = ['닥터 스트레인지', '스플릿','럭키']


# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.

# In[76]:


movie_rank.append('배트맨')


# ## 053 insert(index, item)
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# 
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

# In[79]:


movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨')
movie_rank


# ## 054 del list[index]
# movie_rank 리스트에서 '럭키'를 삭제하라.
# 
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

# In[83]:


movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
del movie_rank[3]
movie_rank


# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# 
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

# In[84]:


movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank = movie_rank[:2]
movie_rank


# 056
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
# 
# >> lang1 = ["C", "C++", "JAVA"]
# >> lang2 = ["Python", "Go", "C#"]
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

# In[85]:


lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
langs


# 057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# 
# nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
# max:  7
# min:  1

# In[89]:


nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))


# 058
# 다음 리스트의 합을 출력하라.
# 
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15

# In[91]:


nums = [1, 2, 3, 4, 5]

print(sum(nums))


# ## 059 len()
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
# 
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

# In[97]:


cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))


# 060
# 다음 리스트의 평균을 출력하라.
# 
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0

# In[99]:


print(sum(nums)/len(nums))


# # 061 ~ 070

# 061
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# 
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]

# In[104]:


price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


# 062
# 슬라이싱을 사용해서 홀수만 출력하라.
# 
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]

# In[105]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])


# 063
# 슬라이싱을 사용해서 짝수만 출력하라.
# 
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]

# In[106]:


print(nums[1::2])


# 064
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# 
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]

# In[107]:


nums = [1, 2, 3, 4, 5]
print(nums[::-1])


# 065
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# 
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 
# 출력 예시:
# 삼성전자 Naver

# In[110]:


interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])


# ## 066 join 메서드 [string.join(list)]
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# 
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

# In[112]:


interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))


# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# 
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

# In[113]:


interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))


# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# 
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

# In[114]:


interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))


# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# 
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

# In[103]:


string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)


# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.
# 
# data = [2, 4, 3, 1, 5, 10, 9]

# In[102]:


data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)


# # 071 ~ 080

# 071
# my_variable 이름의 비어있는 튜플을 만들라.

# In[115]:


my_variable = ()


# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키

# In[116]:


movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
movie_rank


# ## 073
# 숫자 1 이 저장된 튜플을 생성하라.

# In[119]:


t = (1)
type(t) #int로 나옴

t = (1,)
type(t)


# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# 
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# In[120]:


t = (1, 2, 3)
t[0] = 'a'
# 튜플은 값을 변경할 수 없다.


# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# 
# t = 1, 2, 3, 4

# In[124]:


t = 1, 2, 3, 4
type(t) # 튜플 : 사용자 편의를 위해 괄호 없이도 동작한다.


# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# 
# t = ('a', 'b', 'c')

# In[126]:


t = ('a', 'b', 'c')
t = ('A', 'b', 'c') # slicing 등으로 수정 불가, 새로운 튜플생성
t


# 077
# 다음 튜플을 리스트로 변환하라.
# 
# interest = ('삼성전자', 'LG전자', 'SK Hynix')

# In[130]:


interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
interest


# 078
# 다음 리스트를 튜플로 변경하라.
# 
# interest = ['삼성전자', 'LG전자', 'SK Hynix']

# In[131]:


interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
interest


# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
# 
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# In[135]:


temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake
type(a) #string 으로 튜플의 개별값이 할당


# ## 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# 
# (2, 4, 6, 8 ... 98)

# In[147]:


a = tuple(range(2,99,2))
print(a)


# # 081 ~ 090

# ## 081 별 표현식 [*star exp, _. _. = list ==> tuple]
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# 
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
# 
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# In[162]:


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, _, _, = scores
valid_score


# 082
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
# 
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# In[164]:


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_, _, *valid_score = scores
valid_score


# 083
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
# 
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# In[167]:


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_, *valid_score, _ = scores
valid_score


# 084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.

# In[169]:


temp = {}
type(temp)


# 085
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# 
# 이름	희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800

# In[171]:


아이스크림 = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}
아이스크림


# ## 086 딕셔너리 추가
# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
# 
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500

# In[175]:


아이스크림
아이스크림["죠스바"] = 1200
아이스크림["월드콘"] = 1500
아이스크림


# 087
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
# 
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# 실행 예:
# 메로나 가격: 1000

# In[178]:


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print('메로나 가격: %d' %(ice['메로나']))


# 088
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
# 
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# In[179]:


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice['메로나'] = 1300
ice


# ## 089 del component
# 다음 딕셔너리에서 메로나를 삭제하라.
# 
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# In[181]:


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice['메로나']
ice


# 090
# 다음 코드에서 에러가 발생한 원인을 설명하라.
# 
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'

# In[182]:


icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
# '누가바' key값 부존재, 인덱싱 시 에러발생


# # 091 ~ 100

# 091 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
# 
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100

# In[184]:


inventory = {
    '메로나' :	[300,20],
    '비비빅' :	[400,3],
    '죠스바' :	[250,100]
}
inventory


# 092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# 
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 300 원

# In[188]:


inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][0],'원')


# 093 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# 
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 20 개

# In[189]:


inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][1],'개')


# 094 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
# 
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 이름	가격	재고
# 월드콘	500	7
# 실행 예시:
# >> print(inventory)
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

# In[192]:


inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory['월드콘'] = [500, 7]
print(inventory)


# 095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
# 
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# In[195]:


icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice)


# 096 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# 
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# In[197]:


icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
vals = list(icecream.values())
print(vals)


# 097 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# 
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# 출력 예시:
# 6700

# In[205]:


icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# val = list(icecream.values())
# print(sum(val))
print(sum(icecream.values()))


# ## 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
# 
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}

# In[206]:


icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)


# ## 099 zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
# 
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

# In[191]:


keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals)) # 1:1로 key-value 매칭
print(result)


# 100 zip과 dict
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
# 
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

# In[208]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print(close_table)

