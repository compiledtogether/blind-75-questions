# 4Sum or KSum with K = 4

## Topic:
Array, Recursion, Hashing, Two Pointers (kSum generalization)

## Problem:
Find all unique quadruplets `[a, b, c, d]` in the array such that `a + b + c + d == target`.

### Example:
```python
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

---

## Approach: kSum (Generic Recursive)

### 1. Sort the array.
### 2. Use recursive `kSum()` function to reduce to 2Sum problem.
### 3. In `kSum()`:
- If `k == 2`, solve with hash set (2Sum).
- If `k > 2`, for each unique number, reduce the problem to `(k-1)Sum`.

### 4. Use early pruning for optimization:
- If average required is out of range of current `nums`, return early.

---

## Test Cases

# Test Cases

nums1 = [1,0,-1,0,-2,2]
target1 = 0
output1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums2 = [2,2,2,2,2]
target2 = 8
output2 = [[2,2,2,2]]

print(fourSum(nums=nums1, target=target1) == output1)
print(fourSum(nums=nums2, target=target2) == output2)

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n^(k-1)) in average case |
| Space      | O(n) recursion stack + result list |

---

## Notes:
- Skips duplicates using `nums[i-1] != nums[i]`.
- Can be reused for 3Sum, 5Sum by changing the `k` value.