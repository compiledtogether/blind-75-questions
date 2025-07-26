# https://leetcode.com/problems/jump-game
from typing import List
def canJump(nums: List[int]) -> bool:
    maxReach = 0
    for i in range(len(nums)):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
        if maxReach >= len(nums) - 1:
            return True
    
    return False
    
# Test Case

nums = [3, 2, 1, 0, 4]
output = False
# nums = [2, 3, 1, 1, 4]
# output = True

print(canJump(nums) == output)
    
# Time complexity: O(n)
# Space complexity: O(1)