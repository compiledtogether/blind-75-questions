# https://leetcode.com/problems/permutation-in-string/

def checkInclusion(s1: str, s2: str) -> bool:
    # if len(s1) > len(s2): return False

    # s1Count, s2Count = {}, {}

    # for i in range(len(s1)):
    #     s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
    #     s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

    # if s1Count == s2Count:
    #     return True

    # left = 0
    # for right in range(len(s1), len(s2)):
    #     s2Count[s2[right]] = 1 + s2Count.get(s2[right],0)
    #     s2Count[s2[left]] -= 1

    #     if s2Count[s2[left]] == 0:
    #         del s2Count[s2[left]]

    #     left += 1

    #     if s1Count == s2Count:
    #         return True

    # return False

    # # Another approach without using Hashmap
    if len(s1) > len(s2):
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    # Initialize frequency counts for s1 and the first window in s2
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # Slide the window over s2
    for i in range(len(s2) - len(s1)):
        if s1Count == s2Count:
            return True
        s2Count[ord(s2[i]) - ord('a')] -= 1
        s2Count[ord(s2[i + len(s1)]) - ord('a')] += 1

    # Check the last window
    return s1Count == s2Count

# Test Case

s1 = "ab"
s2 = "eidbaooo"
output = True

print(checkInclusion(s1, s2) == output)

# Time Complexity: O(n)
# Space Complexity: O(26)

