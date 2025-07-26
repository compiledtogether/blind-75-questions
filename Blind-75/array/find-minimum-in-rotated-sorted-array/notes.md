# Find minimum in Rotated Sorted Array

## Topics
- Arrays
- Binary Search

---

## Explanation

Apply modified binary search

### Algorithm

1. Take two pointers, left and right, and run the loop till left is smaller than right
2. Find `mid = (left + right) // 2`, check if the element at right index is greater than mid, if yes, element must be left half, so update right to mid.
3. Else, element must be in right half, so update left to mid + 1.
4. Finally, when the loop will break, element will be the one pointed by left, return it.

---

## Test Cases

**Input:** 
nums = [3,4,5,1,2]

**Output:** 
Output = 1

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(logn)  |
| Space      | O(1)  |



