class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1] # We initialize the stack with a base -1
        
        # we iterate through each character of the string with its index
        for i, char in enumerate(s):
            if char == "(":
                # If opener parentheses append to stack
                stack.append(i)
            else:
                # Pop the last element
                stack.pop()
                #Stack empty inser a new base for valid substring
                if not stack:
                    stack.append(i)
                else:
                # if not empty update the length
                    max_len = max(max_len, i - stack[-1])
        return max_len