'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''

# 각각의 알파벳에 대하여 ! 

import sys

alphabet = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z']
pos = []

text = sys.stdin.readline().rstrip()
# print(text)

for a in alphabet :
    if a in text :
        pos.append(text.index(a))
    else :
        pos.append(-1)
        
print(*pos)