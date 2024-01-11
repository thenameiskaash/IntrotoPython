def anagram(a, b):
    counta = {}
    countb = {}

    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        counta[a[i]] = 1 + counta.get(a[i],0)
        countb[b[i]] = 1 + countb.get(b[i],0)
    return True
    
print(anagram("ate", "eat"))