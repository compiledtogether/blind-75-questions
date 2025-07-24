def productExceptSelf(nums: list) -> list:
    nums_len = len(nums)
    output = [1] * nums_len

    # # Using DP without space optimization    
    # prefix = [1] * nums_len
    # suffix = [1] * nums_len
    # for i in range(1, nums_len):
    #     prefix[i] = prefix[i-1] * nums[i-1]
    #     suffix[nums_len - i - 1] = suffix[nums_len - i] * nums[nums_len - i]
        
    # for i in range(nums_len):
    #     output[i] = prefix[i] * suffix[i]

    # Using DP with space optimization    
    prefix_product = 1    
    for i in range(nums_len):
        output[i] = prefix_product
        prefix_product *= nums[i]
        
    sufffix_product = 1
    for i in range(nums_len-1,-1,-1):
        output[i] *= sufffix_product
        sufffix_product *= nums[i]
    
    return output


# # Test cases
        
nums1 = [1,2,3,4]
output1 = [24,12,8,6]

nums2 = [-1,1,0,-3,3]
output2 = [0,0,9,0,0]

print(productExceptSelf(nums=nums1) == output1)
print(productExceptSelf(nums=nums2) == output2)