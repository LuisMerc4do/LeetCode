s = "()[]{}"
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    hashmap = {")":"(", "}":"{", "]": "["}
    stack = []
    for item in s:
        if item in hashmap:
            if stack and stack[-1] == hashmap[item]:
                stack.pop(-1)
            else:
                return False
        else:
            stack.append(item)
    return True if not stack else False
print(isValid(s))