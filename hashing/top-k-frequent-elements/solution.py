# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1            
    
    kFrequent = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))        

    return list(kFrequent.keys())[:k]            

# Test Cases:
nums, k = [1,1,1,2,2,3], 2
Output = [1,2]

print(topKFrequent(nums, k) == Output)


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
