# BRUTE WAY 
def isAnagramm(s, t):
    if len(s) != len(t):
        return False
    hasSeen = []
    for i in s: 
        hasSeen.append(i)
    for t in t: 
        if t in hasSeen:
            hasSeen.remove(t)
        else:
            return False
    return (len(hasSeen) == 0)

# OPTIMIZED WAY 
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
print(isAnagram("anagram", "nagaram"))