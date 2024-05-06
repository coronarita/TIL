import re
import collections

paragraph = input()
ban = eval(input())

def mostCommonWords(paragraph, ban):
    
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    .lower().split()
    if word not in ban]
    
    counts = collections.defaultdict(int)  #important to fill the type [error]
    for word in words :
        
        counts[word] += 1

    return max(counts, key=counts.get) # get key of maximum dict



print(mostCommonWords(paragraph=paragraph, ban=ban))