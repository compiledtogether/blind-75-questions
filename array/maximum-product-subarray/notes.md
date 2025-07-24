# Maximum Product Subarray

## Topics
- Array

---

## Explanation

Use Kadane's algorithm from left to right, then right to left

### Algorithm

1. Iterate the array, to find the max product of the subarray from left to right. If current product becomes 0, make it 1, to recheck further.
2. Iterate the array, to find the max product of the subarray from right to left with the same max product. If current product becomes 0, make it 1, to recheck further.
3. Return max product

--- 

## Test Cases

**Input:**
nums1 = [2,3,-2,4]
**Output:**
output1 = 6

**Input:**
nums2 = [-2,0,-1]
**Output:**
output2 = 0

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |