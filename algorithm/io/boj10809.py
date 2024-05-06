s = input()
from collections import defaultdict

alpha_dict = defaultdict()
# print(alpha_dict)
# initialization
for char in "abcdefghijklmnopqrstuvwxyz" :
    alpha_dict[char] = -1
# print(alpha_dict)
for idx, char in enumerate(s) : # baekjoon
    # print(idx, char)
    if char in alpha_dict.keys() and alpha_dict[char] == -1 :
        alpha_dict[char] = idx

print(*alpha_dict.values())