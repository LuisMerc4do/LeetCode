def decodeString(s):
    stack = []
    current_string = ""
    current_number = 0
    
    for char in s:
        if char == "[":
            stack.append(current_string)
            stack.append(current_number)
            current_string = ""
            current_number = 0
        elif char == "]":
            num = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + num * current_string
        elif char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            current_string += char
    return current_string

class Solution:
    def decodeString(self, s: str):
        stack = []  # Stack to store previous strings and numbers
        current_string = ""  # String being built at the current level
        current_number = 0  # Number representing how many times to repeat a string

        for char in s:  # Loop through each character in the input string
            if char == "[":  # Start of a new block (e.g., "3[abc]")
                # Push current string and number to stack and reset for new block
                stack.append(current_string)
                stack.append(current_number)
                current_string = ""  # Reset for new inner string
                current_number = 0  # Reset for new repeat count
            elif char == "]":  
                # End of a block, time to decode
                num = stack.pop()  # Retrieve the repeat count from stack
                previous_string = stack.pop()  # Retrieve the string before the block
                # then previous_string = 'abc', num = 3, and current_string = 'xy'.
                # So, current_string becomes 'abc' + 3 * 'xy' -> 'abcxyxyxy'.
                current_string = previous_string + num * current_string
            elif char.isdigit():  # If it's a digit, update the current number
                current_number = current_number * 10 + int(char)
            else:  # It's a letter, so add it to the current string
                current_string += char
        return current_string  # Return the fully decoded string
