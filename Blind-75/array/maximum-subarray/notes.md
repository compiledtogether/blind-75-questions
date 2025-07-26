# Maximum Sum Subarray

## Topics
- Array

---

## Explanation

Use Kadane's algorithm

### Algorithm

1. Iterate the array, to find the max sum of the subarray from left to right. If current sum is less than 0, make it 0, to recheck further.

--- 

## Test Cases

**Input:**
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
**Output:**
output1 = 6

**Input:**
nums2 = [5,4,-1,7,8]
**Output:**
output2 = 23

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |