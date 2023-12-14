s = eval(input())  # for input list (or any equation function : using eval())
# print(type(s))

# def reverse_string1(s):
    # s.reverse()


def reverse_string2(s): # 구현 알고리즘을 위한 공부임, 내장함수를 사용해서 풀수도 있지만 ! 
    # swap using two pointers [as traditional]
    left, right = 0, len(s) - 1  # 항상, 좌 인덱스 0, 우 인덱스 size -1
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1




# reverse_string1(s)

reverse_string2(s)
print(s)

