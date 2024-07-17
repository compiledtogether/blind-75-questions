def maxSumSubArray(nums: list) -> int:
    result = nums[0]
    total = 0
    
    for num in nums:
        if total < 0:
            total = 0
        total += num

        result = max(result, total)

    return result
    # maxsum = result = nums[0]
    
    # for num in nums[1:]:
    #     maxsum = max(num, maxsum + num)
    #     result = max(result, maxsum)
        
    # return result

# Test cases
        
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
output1 = 6

nums2 = [1]
output2 = 1

nums3 = [5,4,-1,7,8]
output3 = 23

print(maxSumSubArray(nums=nums1) == output1)
print(maxSumSubArray(nums=nums2) == output2)
print(maxSumSubArray(nums=nums3) == output3)