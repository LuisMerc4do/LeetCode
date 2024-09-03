def canConstruct(ransomNote, magazine):
    hasSeen = []
    for i in magazine: 
        hasSeen.append(i)
    print(hasSeen)
    for i in ransomNote:
        if i in hasSeen:
            hasSeen.remove(i)
        else:
            return False
    return True
    
print(canConstruct("aa", "aab"))

def canConstruct(self, ransomNote, magazine):
    counter = {}
    for i in magazine: 
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for e in ransomNote:
        if e in counter and counter[e] > 0:
            counter[e] -= 1
        else:
            return False
    return True