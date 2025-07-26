# https://leetcode.com/problems/two-sum/

def twoSum(nums: list, target: int) -> list:
    numMap = {}
    for index in range(len(nums)):
        compliment = target - nums[index]
        if compliment in numMap:
            return [numMap[compliment], index]
        numMap[nums[index]] = index
    
    return []

# Test Cases

nums1 = [2,7,11,15] 
target1 = 9
output1 = [0,1]

nums2 = [3,2,4]
target2 = 6
output2 = [1,2]

nums3 = [3,3]
target3 = 6
output3 = [0,1]

print(twoSum(nums=nums1, target=target1) == output1)
print(twoSum(nums=nums2, target=target2) == output2)
print(twoSum(nums=nums3, target=target3) == output3)

# Time Complexity: O(n)
# Space Complexity: O(n)