# https://leetcode.com/problems/max-consecutive-ones-iii

from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    longest, left = 0,0
    counts = [0] * 2

    for right in range(len(nums)):
        # increment the occurence of right pointer
        counts[nums[right]] += 1

        # as we slide the window, decrement the occurence of left pointer, shift left counter 

        # valid condition of substring, if the difference between 
        # window length (r-l)+1 and max(counts) (maximum times any character appears) is greater than k, \
        # i.e. we need to make those changes
        while (right-left) + 1 - counts[1] > k:
            counts[nums[left]] -= 1
            left += 1

        # check which is longest, longest or current window length
        longest = max(longest, (right-left)+1)

    return longest


# Test Case

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
output = 6

print(longestOnes(nums,k) == output)