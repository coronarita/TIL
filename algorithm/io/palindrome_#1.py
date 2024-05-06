s = "A man, a plan, a canal: Panama"
import time

def palindrome1(s:str) -> bool :
    # general solution
    s_list = []
    # preprocessing
    for char in s :
        if char.isalnum():
            s_list.append(char.lower())

    # check
    while len(s_list) > 1 :
        if s_list.pop(0) != s_list.pop():
            return False
    return True
    

def palindrome2(s:str) -> bool :
# general solution using deque
    from collections import deque

    s_list = deque()

    # preprocessing
    for char in s :
        if char.isalnum():
            s_list.append(char.lower())
    
    # check
    while len(s_list) > 1 :
        if s_list.popleft() != s_list.pop():
            return False
    return True

def palindrome3(s:str) -> bool :
    # using regex, slicing
    import re

    # preprocessing
    s = re.sub("[^a-z0-9]", "", s.lower())

    # check
    s_rev = s[::-1]

    if s != s_rev : 
        return False
    return True
import time
s1 = time.time()
print(palindrome1(s))
last = time.time()
print(last - s1)

s1 = time.time()
print(palindrome2(s))
last = time.time()
print(last - s1)

s1 = time.time()
print(palindrome3(s))
last = time.time()
print(last - s1)
