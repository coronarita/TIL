print("섭씨를 화씨로 변환해주는 프로그램")
print("섭씨온도를 입력해주세요:")
cel_value = float(input())
fah_value = ((9/5)* (cel_value))+32
print(f"섭씨온도 :{cel_value:.2f}")
print(f"화씨온도 :{fah_value:.2f}")