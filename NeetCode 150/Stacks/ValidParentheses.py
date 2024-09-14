def isValid(s):
    stack = []
    mapping = {")" : "(", "}":"{", "]":"["}
    
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

def isValid(s):
    # Initialize an empty stack to keep track of opening brackets.
    stack = []
    # Define a mapping of closing to opening brackets for easy lookup.
    mapping = {")": "(", "}": "{", "]": "["}
    # Iterate through each character in the input string.
    for char in s:
        # If the character is a closing bracket.
        if char in mapping:
            # If the stack is empty or the top of the stack does not match the corresponding opening bracket, return False.
            if not stack or stack[-1] != mapping[char]:
                return False
            # Pop the top element from the stack since it matches the current closing bracket.
            stack.pop()
        else:
            # If it's an opening bracket, push it onto the stack.
            stack.append(char)
    # If the stack is empty at the end, all brackets were matched correctly.
    return len(stack) == 0
