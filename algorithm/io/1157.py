"""
Mississipi - ? 그 외 최대 문자
"""

def countLetters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter

word = input()
word = word.upper()
w_count = countLetters(word)

# list comprehension
cond = [k for k, v in w_count.items() if v == max(w_count.values())]
# # print(w_count)
# # cond = [w_count.get(max(w_count.values()))]
# print(cond)
if len(cond) != 1 :
    print('?')
else : 
    print(*cond)