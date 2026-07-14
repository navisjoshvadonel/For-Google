def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # closing → opening

    for char in s:
        if char in mapping:
            # it's a closing bracket
            top = stack.pop() if stack else '#'  # pop or dummy value
            if mapping[char] != top:
                return False
        else:
            # it's an opening bracket
            stack.append(char)

    return len(stack) == 0  # valid only if stack is empty at end

# Test
print(isValid("()"))      # True
print(isValid("()[]{}")), # True
print(isValid("(]"))      # False
print(isValid("([)]"))    # False
print(isValid("{[]}"))    # True