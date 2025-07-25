# https://leetcode.com/problems/subarray-sum-equals-k

from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    prefixSum, result, currSum = {0:1}, 0, 0
    
    for num in nums:
        currSum += num
        diffSum = currSum - k

        result += prefixSum.get(diffSum, 0)
        prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        # if diffSum in prefixSum:
        #     result += prefixSum[diffSum]
        # if currSum in prefixSum:
        #     prefixSum[currSum] += 1
        # else:
        #     prefixSum[currSum] = 1

    return result

# Test Cases:

nums = [1,1,1]
k = 2
Output= 2

print(subarraySum(nums, k) == Output)


