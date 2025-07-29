# https://leetcode.com/problems/longest-palindrome/
def longestPalindrome(s: str) -> int:
    hmap = {}
    count = 0
    flag = False

    for ch in s:
        hmap[ch] = 1 + hmap.get(ch, 0)

    for val in hmap.values():
        if val % 2:
            count += val - 1
            flag = True # If the value is odd, one char will be in middle
        else:
            count += val

    return count + 1 if flag else count

# Test Case:
s = "abccccdd"
output = 7

print(longestPalindrome(s) == output)
