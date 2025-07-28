# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        if (numbers[left]+numbers[right]) == target:
            return [left+1, right+1]
        elif (numbers[left]+numbers[right]) > target:
            right -= 1
        else:
            left += 1
    return []

# Test Case

numbers = [2,7,11,15]
target = 9
Output= [1,2]

print(twoSum(numbers, target) == Output)