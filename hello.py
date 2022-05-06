# 과제 : 1부터 20까지 반복, 그 과정에서 3의 배수일 경우 year 출력
# 나머지 모든 경우 숫자 출력
# 추가 과제1 : 5의배수 dream 출력
# 추가과제2 : 15의 배수 yeardream 출력

print("hello")

for i in range(1,21) :
	if(i % 3) == 0 :
		print("year")
	elif( i% 5) == 0 : 
		print("dream")
	else :
		print(i)
