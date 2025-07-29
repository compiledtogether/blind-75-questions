# https://leetcode.com/problems/valid-parentheses

def isValid(s: str) -> bool:
    stack = []
    d = {'(':')', '{':'}','[':']'}
    for ch in s:
        if ch in '[({':
            stack.append(ch)
        elif len(stack) == 0 or ch != d[stack.pop()]:
            return False

    return not stack

# Test Case:

s = "()[]{}"
output = True

print(isValid(s) == output)