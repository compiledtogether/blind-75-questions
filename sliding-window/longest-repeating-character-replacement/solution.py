# https://leetcode.com/problems/longest-repeating-character-replacement/description/

def characterReplacement(s: str, k: int) -> int:
    longest, left = 0,0
    counts = [0] * 26

    for right in range(len(s)):
        # increment the occurence of right pointer
        counts[ord(s[right]) - 65] += 1

        # as we slide the window, decrement the occurence of left pointer, shift left counter 

        # valid condition of substring, if the difference between 
        # window length (r-l)+1 and max(counts) (maximum times any character appears) is greater than k, \
        # i.e. we need to make those changes
        while (right-left) + 1 - max(counts) > k:
            counts[ord(s[left]) - 65] -= 1
            left += 1

        # check which is longest, longest or current window length
        longest = max(longest, (right-left)+1)

    return longest


# Test Case

s = "ABAB" 
k = 2
output = 4

print(characterReplacement(s,k) == output)

# Time Complexity: O(n)
# Time Complexity: O(1)