#remove outermost parentheses from a string

#stack-based approacj (for nested parentheses)

def remove_outer(s):
    stack = []
    result = []
    
    for char in s:
        if char == '(':
            if stack:
                result.append(char)
            stack.append(char)
        elif char == ')':
            stack.pop()
            if stack:
                result.append(char)
    
    return ''.join(result)
