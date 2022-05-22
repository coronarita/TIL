#!/usr/bin/env python
# coding: utf-8

# # 201 ~ 210

# 201
# "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.

# In[1]:


def print_coin():
    print("비트코인")


# 202
# 201번에서 정의한 함수를 호출하라.

# In[2]:


print_coin()


# 203
# 201번에서 정의한 print_coin 함수를 100번호출하라.

# In[3]:


for i in range(100) : print_coin()


# 204
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.

# In[5]:


def print_coins():
    for i in range(100):
        print("비트코인")
        
print_coins()


# 205
# 아래의 에러가 발생하는 이유에 대해 설명하라.
# 
# hello()
# def hello():
#     print("Hi")
# 실행 예
# 
# NameError: name 'hello' is not defined

# In[7]:


def hello():
    print("Hi")

hello()

# prob : 정의가 되기 전 호출되었기 때문에, NameError: name 'hello' is not defined 의 에러가 발생


# ## 206 def은 실행되지않음
# 아래 코드의 실행 결과를 예측하라.
# 
# def message() :
#     print("A")
#     print("B")
# 
# message()
# print("C")
# message()

# In[8]:


'''
A
B
C
A
B
'''

def message() :
    print("A")
    print("B")

message()
print("C")
message()


# 207
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# 
# print("A")
# 
# def message() :
#     print("B")
# 
# print("C")
# message()

# In[9]:


'''
A
C
B
'''
print("A")

def message() :
    print("B")

print("C")
message()


# 208
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# 
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# In[10]:


'''
A
C
B
E
D
'''

print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()


# 209
# 아래 코드의 실행 결과를 예측하라.
# 
# def message1():
#     print("A")
# 
# def message2():
#     print("B")
#     message1()
# 
# message2()

# In[11]:


'''
B
A
'''
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()


# 210
# 아래 코드의 실행 결과를 예측하라.
# 
# def message1():
#     print("A")
# 
# def message2():
#     print("B")
# 
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# 
# message3()

# In[12]:


'''
B
C
B
C
B
C
A
'''
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


# # 211 ~ 220

# 211
# 함수의 호출 결과를 예측하라.
# 
# def 함수(문자열) :
#     print(문자열)
# 
# 함수("안녕")
# 함수("Hi")

# In[13]:


# 안녕
# Hi

def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")


# 212
# 함수의 호출 결과를 예측하라.
# 
# def 함수(a, b) :
#     print(a + b)
# 
# 함수(3, 4)
# 함수(7, 8)

# In[14]:


#7
#15
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)


# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# 
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# In[ ]:


# 함수() 호출 시 소괄호 내의 argument가 빠져서, print 해야할 게 null값이기 때문에 오류가 남


# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# 
# def 함수(a, b) :
#     print(a + b)
# 
# 함수("안녕", 3)
# TypeError: must be str, not int

# In[ ]:


# 함수 a b는 + 연산이 가능해야하는데, ,str과 int 간에는 합연산이 불가능


# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

# In[15]:


# print_with_smile

def print_with_smile(str):
    print(str+":D")


# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.

# In[16]:


print_with_smile("안녕하세요")


# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

# In[19]:


# print_upper_price
def print_upper_price(price):
    print(price*1.3)
    
print_upper_price(100)


# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.

# In[20]:


#print_sum

def print_sum(a,b):
    print(a+b)
    
print_sum(1,2)


# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# 
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

# In[22]:


#print_arithmetic_operation

def print_arithmetic_operation(a, b):
    print(f"{a}+{b} = {a+b}")
    print(f"{a}-{b} = {a-b}")
    print(f"{a}*{b} = {a*b}")
    print(f"{a}/{b} = {a/b}")
    
print_arithmetic_operation(3, 4)


# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

# In[26]:


# print_max

def print_max(a,b,c):
    if a>b:
        if b>c: print(a)
        else :
            if a>c : print(a)
            else : print(c)
    elif b>c:
        if c>a: print(b)
        else :
            if b>a : print(b)
            else : print(a)
# c>a
    else :
        if a>b: print(c)
        else :
            if c>b : print(c)
            else : print(b)

print_max(1,2,3)


# # 221 ~ 230

# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# 
# print_reverse("python")
# nohtyp

# In[27]:


#print_reverse()

def print_reverse(str):
    str = str[::-1]
    print(str)


print_reverse("python")


# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# 
# print_score ([1, 2, 3])
# 2.0

# In[28]:


# print_score()

def print_score(list):
    print(sum(list)/len(list))
    
print_score ([1, 2, 3])


# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# 
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12

# In[29]:


#print_even()

def print_even(list):
    for i in list:
        if i%2 ==0: print(i)


print_even ([1, 3, 2, 10, 12, 11, 15])


# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# 
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별

# In[35]:


#print_keys

def print_keys(dic):
    for i in dic:
        print(i[:])
        

print_keys ({"이름":"김말똥", "나이":30, "성별":0})


# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# 
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# 
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]

# In[36]:


# print_value_by_key
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(a,b):
    print(a[b])

print_value_by_key  (my_dict, "10/26")


# ## 226 ref number 두기
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# 
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

# In[54]:


# print_5xn

def print_5xn(string):
    ref = int(len(string)/5)
#    for i in range(int(len(string))/5+1): # TypeError: 'float' object cannot be interpreted as an integer
    for i in range(ref+1):
        print(string[5*i:5*i+5])

print_5xn("아이엠어보이유알어걸")


# 
# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# 
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

# In[56]:


# print_mxn

def print_mxn(string, j):
    ref = int(len(string)/j)
#    for i in range(int(len(string))/j+1): # TypeError: 'float' object cannot be interpreted as an integer
    for i in range(ref+1):
        print(string[j*i:j*i+j])

print_mxn("아이엠어보이유알어걸", 3)


# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# 
# calc_monthly_salary(12000000)
# 1000000

# In[75]:


# calc_monthly_salary(annual_salary)

def calc_monthly_salary(annual_salary):
#    monthly_salary = annual_salary/12
#    print(monthly_salary-monthly_salary%10)
    
    monthly_salary = int(annual_salary/12)
    return monthly_salary

calc_monthly_salary(1200000)


# 229
# 아래 코드의 실행 결과를 예측하라.
# 
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print"오른쪽:", b)
# 
# my_print(a=100, b=200)

# In[78]:


def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)


# 230
# 아래 코드의 실행 결과를 예측하라.
# 
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# 
# my_print(b=100, a=200)

# In[79]:


def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)


# # 231 ~ 240

# 231
# 아래 코드를 실행한 결과를 예상하라.
# 
# def n_plus_1 (n) :
#     result = n + 1
# 
# n_plus_1(3)
# print (result)

# In[80]:


#error (result는 local variable) 
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print(result)


# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# 
# make_url("naver")
# www.naver.com

# In[84]:


#make_url

def make_url(url):
#    print(f"www.{url}.com")
    url = "www."+url+".com"
    return url
    
make_url("naver")


# ## 233 string을 for문의 range로 입력받으면! char 하나하나가 변수가 됩니다.
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# 
# make_list("abcd")
# ['a', 'b', 'c', 'd']

# In[104]:


# make_list

def make_list(str):
    my_list = []

    for i in str:
        print(i)
        my_list.append(i)
    return my_list

make_list("abcd")


# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# 
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

# In[105]:


#pickup_even

def pickup_even(my_list):
    save_list = []
    for i in my_list:
        if i%2 ==0 :
            save_list.append(i)
    return save_list

pickup_even([3, 4, 5, 6, 7, 8])


# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# 
# convert_int("1,234,567")
# 1234567

# In[ ]:


#convert_int

def convert_int(str):
    a = 

convert_int("1,234,567")


# 236
# 아래 코드의 실행 결과를 예측하라.
# 
# def 함수(num) :
#     return num + 4
# 
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# In[ ]:


# 22


# 237
# 아래 코드의 실행 결과를 예측하라.
# 
# def 함수(num) :
#     return num + 4
# 
# c = 함수(함수(함수(10)))
# print(c)

# In[ ]:


# 22


# 238
# 아래 코드의 실행 결과를 예측하라.
# 
# def 함수1(num) :
#     return num + 4
# 
# def 함수2(num) :
#     return num * 10
# 
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# In[ ]:


#140


# 239
# 아래 코드의 실행 결과를 예측하라.
# 
# def 함수1(num) :
#     return num + 4
# 
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
# 
# c = 함수2(10)
# print(c)

# In[ ]:


# 16


# 240
# 아래 코드의 실행 결과를 예측하라.
# 
# def 함수0(num) :
#     return num * 2
# 
# def 함수1(num) :
#     return 함수0(num + 2)
# 
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
# 
# c = 함수2(2)
# print(c)

# In[ ]:


# 28


# # 241 ~ 250

# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.

# In[4]:


import datetime


# In[11]:


t = datetime.datetime.now()
print(t)


# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

# In[13]:


print(type(t))


# ## 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

# In[15]:


# timedelta : 날짜의 차이를 days에 받음
for day in range( 5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = t - delta
    print(date)


# ## 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 
# 18:35:01 

# In[26]:


# strftime : 시간만 slicing해서 형식에 맞게 출력?
time = datetime.datetime.now()
print(time.strftime("%H:%M:%S"))


# ## 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
# 
# 
# 
# 
#  

# In[28]:


day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(day, type(day), ret, type(ret))


# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

# In[ ]:


import time
import datetime

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)


# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.

# In[ ]:


import os #os.rename() : 가장 단순
from os import rename() # rename() 모듈이름 생략가능
from os import * # getcwd(), rename()
import os_import myos #myos.rename()모듈이름이 길 때, 짧게 쓸 수 있지


# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

# In[1]:


import os

direc = os.getcwd()
print(direc)


# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.

# In[3]:


os.rename("/Users/Kimdaseul/Desktop/무제.txt","/Users/Kimdaseul/Desktop/무제2.txt")


# ## 250 numpy - arange : 구간 및 increment 설정 시 list로 반환
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.

# In[5]:


#arange :
import numpy as np

for i in np.arange(0, 5, 0.1):
    print(i)


# # 251 ~ 260

# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.
# 

# In[ ]:


# 클래스 : 객체, 인스턴스의 설계도
# 객체 : '일발적인 클래스로부터 만들어 진'
# 인스턴스 : 'A'라는 강조하고싶은, 클래스로부터 만들어 진 객체 


# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.

# In[6]:


class Human :
    pass


# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.

# In[7]:


class Human :
    pass

areum = Human()
        


# ## 254 클래스 생성자-1 : constructor
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
# 
# >>> areum = Human()
# 응애응애

# In[9]:


class Human :
    def __init__(self):
        print("응애응애")

areum = Human()
        


# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# 
# >>> areum = Human("아름", 25, "여자")

# In[13]:


class Human :
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")


# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
# 
# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예
# 
# >>> areum.age
# 25

# In[15]:


class Human :
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.age)


# ## 257 클래스 메소드 - 1 : class 내부에 def 시에 self 넣어줘야 호출가능
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
# 
# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자

# In[22]:


class Human :
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self) :
        print(self.name, self.age, self.sex)
areum = Human("아름", 25, "여자")

areum.who()


# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# 
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")

# In[24]:


class Human :
    
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self) :
        print(self.name, self.age, self.sex)

       
        
areum = Human("모름", 0, "모름")
areum.who()

areum.setInfo("아름", 25, "여자")
areum.who()


# 
# ## 259 클래스 소멸자 : __del__(self):
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# 
# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라

# In[25]:


class Human :
    
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지 말라")
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self) :
        print(self.name, self.age, self.sex)



   

areum = Human("모름", 0, "모름")
areum.setInfo("아름", 25, "여자")
del areum


# ## 260 에러의 원인 :  객체에서 . 호출 시 객체명이 자동으로 함수의 argument로 넘어감(self 필요)
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
# 
# class OMG : 
#     def print() :
#         print("Oh my god")
# 
# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()
# 
# TypeError: print() takes 0 positional arguments but 1 was given

# In[26]:


# 기본 제공 메서드랑 충돌 ?
class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock) : .찍어서 함수 호출하면 객체(인스턴스) 아규먼트 자체가 함수의 인자로 들어감.
                    # 그러나, OMG 내 print 함수는 self가 없기때문에 인자를 받지 못함(.호출 시 자동으로 넘어감!)


# In[4]:


class Person:
    
    data_of_class = 100
    
    def method_of_class():
        print("Person class 의 method입니다.")

# Class 자체 명으로 self없이 define 된         
print(Person.data_of_class)
Person.method_of_class()

JH = Person()
print(JH.data_of_class)
JH.method_of_class()


# # 261 ~ 270

# 261 Stock 클래스 생성
# 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.

# In[27]:


class Stock :
    pass


# 262 생성자
# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
# 
# 삼성 = Stock("삼성전자", "005930")

# In[31]:


class Stock:
    def __init__(self, title, code):
        self.title = title
        self.code = code

삼성 = Stock("삼성전자", "005930")
print(삼성.title)
print(삼성.code)


# 263 메서드
# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
# 
# a = Stock(None, None)
# a.set_name("삼성전자")

# In[32]:


class Stock:
    def __init__(self, title, code):
        self.title = title
        self.code = code

    def set_name(self, title):
        self.title = title

a = Stock(None, None)
a.set_name("삼성전자")        
print(a.title)


# 264 메서드
# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.
# 
# a = Stock(None, None)
# a.set_code("005930")

# In[34]:


class Stock:
    def __init__(self, title, code):
        self.title = title
        self.code = code

    def set_name(self, title):
        self.title = title

    def set_code(self, code):
        self.code = code
        
a = Stock(None, None)
a.set_name("삼성전자")        
a.set_code("005930")
print(a.title, a.code)


# 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
# 
# 삼성 = Stock("삼성전자", "005930")

# In[36]:


class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
        
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
        
삼성 = Stock("삼성전자", "005930")
a = 삼성.get_name()
b = 삼성.get_code()

print(a,b)


# 266 객체의 속성값 업데이트
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.

# In[2]:


class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
        
    def set_per(self, per):
        self.per = per
    
    def set_pbr(self, pbr):
        self.pbr = pbr
        
    def set_dividend(self, dividend):
        self.dividend = dividend
        
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code


# 267 객체 생성
# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.
# 
# 항목	정보
# 종목명	삼성전자
# 종목코드	005930
# PER	15.79
# PBR	1.33
# 배당수익률	2.83

# In[4]:


a = Stock("삼성전자","005930",15.79, 1.33, 2.83)


# 268 객체의 속성 수정
# PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

# In[46]:


#266에 추가하였음

# !pip install jupyterthemes
jt -t onedork -fs 115 -nfs 125 -tfs 115 -dfs 115 -ofs 115 -cursc r -cellw 80% -lineh 115 -altmd  -kl -T -N


# 269 객체의 속성 수정
# 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

# In[5]:


a.set_per(12.75)
print(a.per)


# ## 270 여러 종목의 객체 생성 (리스트랑 응용이라서 다시보자)
# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.
# 
# 종목명	종목코드	PER	PBR	배당수익률
# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37

# In[7]:


종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG전자","066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대)
종목.append(LG)

for i in 종목 : 
    print(i.code, i.per)


# # 271 ~ 280

# ## 271 Account 클래스 계좌번호 랜덤하게 생성
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
# 
# 은행이름: SC은행
# 계좌번호: 111-11-111111

# In[10]:


import random

class Account : 
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 +'-'+num3

        
lee = Account("이정훈", 100)
print(lee.name)
print(lee.balance)
print(lee.account_number)
print(lee.bank)


# ### 272 클래스 변수 - 계좌 객체 수 저장 시 예외처리 ? - 조원들과 논의 해 보자.
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

# In[1]:


import random

class Account : 
    bal_num = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 +'-'+num3

        Account.bal_num += 1
        
lee = Account("이정훈", 100)
print(Account.bal_num)
kim = Account("김정훈", 200)
print(Account.bal_num)
lee = Account("이정훈", 100)
print(Account.bal_num)
kim = Account("김정훈", 200)
print(Account.bal_num)


#Test결과, Account가 호출 될 때마다 +1이 됨, 따라서, 중복된 계좌일 때 +하지않는 예외처리는 어떻게 할까 ?에 대한 고민이 필요


# ## 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

# In[20]:


import random

class Account : 
    bal_num = 0
    
    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 +'-'+num3
        
        Account.bal_num += 1

    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

lee = Account("이정훈", 100)
lee.get_account_num()  # Account.get_account_num()


# 274 입금 메서드
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

# In[8]:


import random

class Account : 
    bal_num = 0
    
    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.bal_num += 1

    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

    def deposit(self, input):
        if input > 0 : 
            self.balance += input
            print(self.balance)

lee = Account("이정훈", 100)
lee.get_account_num()  # Account.get_account_num()
lee.deposit(100)


# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
# 
# 
# 
# 
#  

# In[11]:


import random

class Account : 
    bal_num = 0
    
    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.bal_num += 1

    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

    def deposit(self, input):
        if input > 0 : 
            self.balance += input
            print(self.balance)

    def withdraw(self, out):
        if self.balance - out > 0 :
            self.balance -= out
            print(self.balance)
            
lee = Account("이정훈", 100)
lee.get_account_num()  # Account.get_account_num()
lee.deposit(300)
lee.withdraw(200)


# ## 276 정보 출력 메서드 : 구분쉼표 출력 시, "{:,}".format 활용하기
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
# 
# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원

# In[20]:


import random

class Account : 
    bal_num = 0
    
    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.bal_num += 1

    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

    def deposit(self, input):
        if input > 0 : 
            self.balance += input
            print(self.balance)

    def withdraw(self, out):
        if self.balance - out > 0 :
            self.balance -= out
            print(self.balance)

            
    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")

#        print(f"잔고: {self.balance}") # 3자리마다 쉼표 표기를 해야함

        print(f"잔고: {int(self.balance/1000)},{self.balance%1000}") # 3자리마다 쉼표 표기를 해야함
# 정식적인 표기법
        print(f"잔고:" "{:,}".format(self.balance))
            
lee = Account("이정훈", 100)
lee.get_account_num()  # Account.get_account_num()
lee.deposit(1300000)
lee.withdraw(200)
lee.display_info()


# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

# In[56]:


import random

class Account : 
    bal_num = 0

    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.deposit_count = 0       
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.bal_num += 1

    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

    def deposit(self, input):
        if input > 0 : 
            self.balance += input
            self.deposit_count += 1
            print(f" ""{:,}".format(self.balance), end= '') # print 쓴 후 개행하지 않음
            print(f"원 입금! {self.deposit_count}회차")
        if self.deposit_count == 5 :
            self.balance *= 1.01
            print(f"\n{self.deposit_count}회차 입금에 따른 1%의 이자 지급 후 :" "{:,}원\n".format(int(self.balance)))
        
    def withdraw(self, out):
        if self.balance - out > 0 :
            self.balance -= out
            print(f"{out}원 출금 후 잔고:" "{:,}\n".format(int(self.balance)))

            
    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고:" "{:,}".format(int(self.balance)))
            
lee = Account("이정훈", 100)
lee.get_account_num()  # Account.get_account_num()
lee.deposit(1300000)
lee.deposit(1300000)

lee.withdraw(200)
lee.display_info()


# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

# In[65]:


import random

class Account : 
    bal_num = 0
    customer_name = []
     
    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.deposit_count = 0       
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.bal_num += 1
        Account.customer_name.append(name)
        
    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

    def deposit(self, input):
        if input > 0 : 
            self.balance += input
            self.deposit_count += 1
            print(f" ""{:,}".format(self.balance), end= '') # print 쓴 후 개행하지 않음
            print(f"원 입금! {self.deposit_count}회차")
        if self.deposit_count == 5 :
            self.balance *= 1.01
            print(f"\n{self.deposit_count}회차 입금에 따른 1%의 이자 지급 후 :" "{:,}원\n".format(int(self.balance)))
        
    def withdraw(self, out):
        if self.balance - out > 0 :
            self.balance -= out
            print(f"{out}원 출금 후 잔고:" "{:,}\n".format(int(self.balance)))

            
    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고:" "{:,}".format(int(self.balance)))

customer_list = []
lee = Account("이정훈", 10000000)
sam = Account("삼정훈", 100)
sa = Account("사정훈", 20000000)

customer_list.append(lee)
customer_list.append(sam)
customer_list.append(sa)

print(customer_list)


# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

# In[66]:


for i in customer_list : 
    if i.balance>=1000000 : 
        i.display_info()


# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

# In[70]:


import random

class Account : 
    bal_num = 0
    customer_name = []

    def __init__(self, name, balance): # 앞이 self 이면 인스턴트 메서드라고 함
        self.deposit_count = 0       
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        #zfill : 자리수 ? string 앞에 0 채우려고 (숫자가 적을 시에)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.bal_num += 1
        Account.customer_name.append(name)

        self.input_rec = []
        self.output_rec = []
        
    #객체에 접근 할 필요가 없는 메서드를 cls처리해서 self 객체/인스턴스가 넘어오지않게 해 줌
    @classmethod
    def get_account_num(cls): # 객체에서 호출해도 객체 대신 클래스의 이름이 넘어옵니다.
        print(cls.bal_num)

    def deposit(self, input):
        if input > 0 : 
            self.balance += input
            self.deposit_count += 1
            print(f" ""{:,}".format(self.balance), end= '') # print 쓴 후 개행하지 않음
            print(f"원 입금! {self.deposit_count}회차")
            self.input_rec.append(input)
        if self.deposit_count == 5 :
            self.balance *= 1.01
            print(f"\n{self.deposit_count}회차 입금에 따른 1%의 이자 지급 후 :" "{:,}원\n".format(int(self.balance)))
        
    def withdraw(self, out):
        if self.balance - out > 0 :
            self.balance -= out
            print(f"{out}원 출금 후 잔고:" "{:,}\n".format(int(self.balance)))
            self.output_rec.append(out)
            
    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고:" "{:,}".format(int(self.balance)))
        
    def diposit_history(self):
        for i in self.input_rec : 
            print("+",i)
    
    def withdraw_history(self):
        for i in self.output_rec :
            print("-",i)
    
lee = Account("이정훈", 100)
lee.get_account_num()  # Account.get_account_num()
lee.deposit(1300000)
lee.deposit(1300000)
lee.deposit(20000)

lee.withdraw(200)
lee.withdraw(300)

lee.diposit_history()
lee.withdraw_history()


#    # 281 ~ 290

# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요.
# 
# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000

# In[6]:


class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        
car = 차(2, 1000)
car.바퀴
car.가격


# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.

# In[7]:


class 자전차(차):
    pass


# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# 
# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 
# 
# 100

# In[8]:


class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

bicycle = 자전차(2, 100)
bicycle.가격


# ## 284 클래스 상속 super().__init__(var)
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# 
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노

# In[12]:


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격) 
        self.구동계 = 구동계
        
bicycle = 자전차(2, 100, "시마노")
bicycle.구동계


# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
# 
# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000 

# In[17]:


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 {}".format(self.바퀴))
        print("가격 {}".format(self.가격))

car = 자동차(4, 1000)
car.정보()


# 286 부모 클래스 생성자 호출
# 다음 코드가 동작하도록 차 클래스를 수정하세요.
# 
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100

# In[20]:


class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 {}".format(self.바퀴))
        print("가격 {}".format(self.가격))
        
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격) 
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()


# ## 287 부모 클래스 메서드 호출 : 일반함수 상속 시에도 super().함수명(변수)[self 제외]
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
# 
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노

# In[22]:


class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 {}".format(self.바퀴))
        print("가격 {}".format(self.가격))
        
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격) 
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print("구동계 {}".format(self.구동계))
    
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()


# 288 메서드 오버라이딩
# 다음 코드의 실행 결과를 예상해보세요.
# 
# class 부모:
#   def 호출(self):
#     print("부모호출")
# 
# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()

# In[23]:


자식호출


# 289 생성자
# 다음 코드의 실행 결과를 예상해보세요.
# 
# class 부모:
#   def __init__(self):
#     print("부모생성")
# 
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
# 나 = 자식()

# In[24]:


자식생성


# 290 부모클래스 생성자 호출
# 다음 코드의 실행 결과를 예상해보세요.
# 
# class 부모:
#   def __init__(self):
#     print("부모생성")
# 
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()
# 
# 나 = 자식()

# In[25]:


자식생성
부모생성


# # 291 ~ 300

# ## 291 파일 쓰기
# 바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.
# 
# 005930
# 005380
# 035420

# In[26]:


pwd


# In[35]:


f = open("/Users/Kimdaseul/Downloads/파이썬300/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()


# 292 파일 쓰기
# 바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.
# 
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER

# In[28]:


f = open("/Users/Kimdaseul/Downloads/파이썬300/매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER")
f.close()


# 293 CSV 파일 쓰기
# 바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.

# In[31]:


import csv

f = open("/Users/Kimdaseul/Downloads/파이썬300/매수종목.csv", mode="wt", encoding="utf-8", newline='')
# cp949 의 경우 윈도우의 csv 형태에서 사용하는 포멧 ! 
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()


# 294 파일 읽기
# 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.
# 
# 005930
# 005380
# 035420

# In[37]:


f = open("/Users/Kimdaseul/Downloads/파이썬300/매수종목1.txt", encoding="utf-8")
lines = f.readlines() #python list
# lines
codes = []
for line in lines:
    code = line.strip() # '\n'
    codes.append(code)
    
print(codes)
f.close()


# ## 295 파일 읽기 + dictionary 에 쪼개서 저장하기 : strip, split, indexing
# 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.
# 
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER

# In[40]:


f = open("/Users/Kimdaseul/Downloads/파이썬300/매수종목2.txt", encoding="utf-8")
lines = f.readlines() #python list

# lines

data = {}
for line in lines:
     line = line.strip() # '\n'
     k, v = line.split()   
     data[k] = v
    
print(data)
f.close()


# In[49]:


per = ["10.31", "", "8.00"]
try:
    for i in per :
        print(float(i))
except ValueError :
        print(0)


# ## 296 예외처리 : try except
# 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
# 
# per = ["10.31", "", "8.00"]
# 
# for i in per:
#     print(float(i))

# In[43]:


per = ["10.31", "", "8.00"]

for i in per:
    try :
        print(float(i))
    except :
        print(0)


# 297 예외처리 및 리스트에 저장
# 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.
# 
# per = ["10.31", "", "8.00"]
# 
# for i in per:
#     print(float(per))

# In[46]:


per = ["10.31", "", "8.00"]
per_float = []
for i in per:
    try :
        print(float(i))
        per_float.append(float(i))
    except :
        print(0)
        per_float.append(0)
        
per_float


# ## 298 특정 예외만 처리하기 ZeroDivisionError
# 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.

# In[47]:


try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")


# ## 299 예외의 메시지 출력하기 : Error message binding
# 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.
# 
# try:
#     실행코드
# except 예외 as 변수:
#     예외처리코드 
# 리스트의 인덱싱에 대해 에러를 출력해보세요.
# 
# data = [1, 2, 3]
# 
# for i in range(5)
#     print(data[i])

# In[53]:


data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)


# In[55]:


data = [1, 2, 3]

for i in range(5):
    print(data[i])


# 300 try, except, else, finally 구조 사용해보기
# 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.
# 
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드
# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.
# 
# per = ["10.31", "", "8.00"]
# 
# for i in per:
#     print(float(per))

# In[67]:


per = ["10.31", "", "8.00"]

for i in per:
     try:
        print(float(i))
     except:
        print(0)
     else:
         print("Clean data")        
     finally:
         print("Finished")


# In[ ]:




