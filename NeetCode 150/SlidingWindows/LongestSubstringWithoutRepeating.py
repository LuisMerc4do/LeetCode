class Solution:
    def longestSubstringWithoutRepeat(s: str):
        state = set()
        start = 0
        max_ = 0

        for end in range(len(s)):
            while s[end] in state:
                state.remove(s[start])
                start += 1
            
            max_ = max(max_, (end - start) + 1)
            state.add(s[end])
        return max_
    
    print(longestSubstringWithoutRepeat("abcabcbb"))
