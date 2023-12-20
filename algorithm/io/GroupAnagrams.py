text = eval(input())

def groupAnagram(text):
    # using defaultdict
    import collections
    anagram = collections.defaultdict(list)
    ans= []
    # gather !
    for word in text:
        # print(''.join(sorted(word)))  # New snippets I learned! 
        anagram[''.join(sorted(word))].append(word)
    print(list(anagram.values()))

    

groupAnagram(text)