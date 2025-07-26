# Product of Array Except Self

## Topics
- Array
- Prefix Sum

---

## Explanation

Iterate the array, to find prefix product and then suffix product, return the output

### Algorithm

1. Iterate the array, left to right, and in the output array, add all the prefix product first, store prefix in a variable
2. Then, add the suffix product in the output array, store suffix in a variable.
3. Return output array

--- 

## Test Cases

**Input:**
nums1 = [1,2,3,4]
**Output:**
output1 = [24,12,8,6]

**Input:**
nums2 = [-1,1,0,-3,3]
**Output:**
output2 = [0,0,9,0,0]

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |