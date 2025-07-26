# Contains Duplicate

## Topics
- Array
- Hashing
- Set

---

## Explanation

Add element is set, if the same element is already present, return true, else add in set, return false at last.

### Algorithm

#### Approach 1: (Using Set)

1. Iterate list, and check if the element is present in set, if present, return true, else add in set
2. If no duplicate, return false

#### Approach 2: (Using set with one line)

1. Check the length of nums list and length of list of set of nums, if they are equal, return true, else false.

--- 

## Test Cases

**Input:**
nums1 = [1,2,3,1]
**Output:**
output1 = True
**Input:**
nums2 = [1,2,3,4]
**Output:**
output2 = False
**Input:**
nums3 = [1,1,1,3,3,4,3,2,4,2]
**Output:**
output3 = True

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |