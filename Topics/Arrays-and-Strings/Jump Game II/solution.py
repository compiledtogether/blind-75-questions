# https://leetcode.com/problems/jump-game-ii
from typing import List
def jump(nums: List[int]) -> int:
    n = len(nums)
    jumps, current, farthest = 0,0,0

    for i in range(n-1):
        farthest = max(farthest, i + nums[i])
        if i == current:
            jumps += 1
            current = farthest

    return jumps
    
# Test Case

nums = [2,3,1,1,4]

Output= 2

print(jump(nums) == Output)

# Time Complexity: 0(n)
# Space Complexity: 0(1)