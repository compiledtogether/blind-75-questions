# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
    return "".join(sorted(s)) == "".join(sorted(t))

# Test Cases

s,t = "anagram", "nagaram"

print(isAnagram(s,t))

