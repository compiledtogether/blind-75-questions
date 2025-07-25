# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]

# Test Cases

nums = [4,5,6,7,0,1,2]
output = 0

print(findMin(nums) == output)