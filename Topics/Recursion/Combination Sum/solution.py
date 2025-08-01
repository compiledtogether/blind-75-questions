# https://leetcode.com/problems/combination-sum
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[int] = []
        def helper(start: int, currSum: int, curr: List[int]):
            if currSum == target:
                res.append(curr.copy()) # type: ignore
                return

            if currSum > target or start == len(candidates):
                return

            # not pick
            helper(start+1, currSum, curr)
            
            # pick
            curr.append(candidates[start])
            helper(start, currSum + candidates[start], curr)
            curr.pop()

        helper(0,0,[])
        return res # type: ignore

# Time Complexity: O(2^n)
# Space Complexity: O(n)