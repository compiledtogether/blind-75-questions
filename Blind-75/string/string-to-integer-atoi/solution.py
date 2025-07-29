# https://leetcode.com/problems/string-to-integer-atoi

def myAtoi(s: str) -> int:
    s = s.strip()
    if not s: return 0

    negative = False
    i = 0
    if s[0] in '+-':
        negative = True if s[0] == '-' else False
        i += 1

    result = 0
    maxPos = 2147483647 #pow(2, 31) -1
    maxNegative = 2147483648 #pow(2, 31) (could also do -pow if you want it in neg)
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])

        result = result * 10 + digit
        i += 1
    if negative and result > maxNegative:
        result = maxNegative
    if not negative and result > maxPos:
        result = maxPos
    
    return result if not negative else result * -1

# Test Case:

s = " -042"
output = -42

print(myAtoi(s) == output)