# https://leetcode.com/problems/contains-duplicate
def containsDuplicate(nums: list) -> bool:
        # approach one using set
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False
        
        # # approach one using set in one line
        # return len(set(nums)) != len(nums)
      
# Test cases
        
nums1 = [1,2,3,1]
output1 = True

nums2 = [1,2,3,4]
output2 = False

nums3 = [1,1,1,3,3,4,3,2,4,2]
output3 = True

print(containsDuplicate(nums=nums1) == output1)
print(containsDuplicate(nums=nums2) == output2)
print(containsDuplicate(nums=nums3) == output3)