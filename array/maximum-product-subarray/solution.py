def maxProductSubArray(nums: list) -> int:
    # first approach using Kadane's algorithm in both directions
    curr_prod = 1
    max_prod = nums[0]
    
    # left to right Kadane's algorithm
    for num in nums:
        curr_prod *= num
        max_prod = max(curr_prod, max_prod)
        if curr_prod == 0:
            curr_prod = 1
        
    # right to left Kadane's algorithm
    reversed_nums = nums[::-1]
    curr_prod = 1
    for num in reversed_nums:
        curr_prod *= num
        max_prod = max(curr_prod, max_prod)
        if curr_prod == 0:
            curr_prod = 1
        
    return max_prod

    # second approach using current max and min product
    # curr_max_prod = curr_min_prod = max_prod = nums[0]
    # for num in nums[1:]:
    #     if num < 0: curr_max_prod, curr_min_prod = curr_min_prod, curr_max_prod
    #     curr_max_prod = max(num, curr_max_prod * num)
    #     curr_min_prod = min(num, curr_min_prod * num)
    #     max_prod = max(max_prod, curr_max_prod)
    # return max_prod

# Test cases
        
nums1 = [2,3,-2,4]
output1 = 6

nums2 = [-2,0,-1]
output2 = 0

print(maxProductSubArray(nums=nums1) == output1)
print(maxProductSubArray(nums=nums2) == output2)