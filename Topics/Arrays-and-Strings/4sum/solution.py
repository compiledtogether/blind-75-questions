# https://leetcode.com/problems/4sum

def fourSum(nums: list, target: int) -> list:
    def kSum(nums: list, target: int, k: int) -> list:
        result = []
        
        if not nums:
            return result
        
        average = target // k
        
        if average < nums[0] or nums[-1] < average:
            return result
        
        if k == 2:
            return twoSum(nums=nums, target=target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in kSum(nums[i+1 :], target-nums[i], k-1):
                    result.append([nums[i]] + subset)
                    
        return result


    def twoSum(nums: list, target: int) -> list:
        result = []
        numSet = set()
        for index in range(len(nums)):
            if len(result) == 0 or result[-1][1] != nums[index]:
                compliment = target - nums[index]
                if compliment in numSet:
                    result.append([compliment, nums[index]])
            numSet.add(nums[index])
        
        return result

    nums.sort()
    return kSum(nums=nums, target=target, k=4)

# Test Cases

nums1 = [1,0,-1,0,-2,2]
target1 = 0
output1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums2 = [2,2,2,2,2]
target2 = 8
output2 = [[2,2,2,2]]

print(fourSum(nums=nums1, target=target1) == output1)
print(fourSum(nums=nums2, target=target2) == output2)