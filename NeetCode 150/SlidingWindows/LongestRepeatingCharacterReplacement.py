def characterReplacement(s, k):
    state = {}
    max_freq = 0
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) + 1
        # {a :3, b: 1, c: 2} max_freq = a
        max_freq = max(max_freq, state[s[end]])
        
        if k + max_freq < end - start + 1:
            state[s[start]] -= 1
            start += 1
        
        max_length = max(max_length, end - start + 1)
    return max_length