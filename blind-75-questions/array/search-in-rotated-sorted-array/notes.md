# Search in Rotated Sorted Array

## Topics
- Arrays
- Binary Search

---

## Explanation

Apply modified binary search

### Algorithm

1. Use the common end statment to check if the target is equal to middle, `middle = (left + right) // 2`
2. Find out if the left is sorted, if yes, check if target lies between left most value and mid value, 
if yes, then update right by mid - 1, else, update left by mid + 1
3. Find out if the right is sorted, if yes, check if target lies between mid value and right most value, if yes, then update left by mid + 1, else update right by mid - 1.

---

## Test Cases

**Input:** 
nums = [4,5,6,7,0,1,2]
target = 0

**Output:** 
Output = 4

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(logn)  |
| Space      | O(1)  |



