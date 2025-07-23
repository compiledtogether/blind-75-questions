# Three Sum

## Topic
- Array
- Two Pointers
- Sorting

## Problem
Given an integer array `nums`, return all the unique triplets `[a, b, c]` such that `a + b + c == 0`.

### Example
```python
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

## Explanation

### Algorithm

1. **Sort the array** to manage duplicates and apply the two-pointer approach.
2. Fix one number `a = nums[i]` at a time.
   - Skip duplicates for `a` to avoid repeated triplets.
3. Use two pointers `l` (left) and `r` (right) to find the other two numbers.
   - If the sum is too big, move `r` left.
   - If the sum is too small, move `l` right.
   - If the sum is exactly zero, save the triplet and skip duplicates for `l` and `r`.

---

## 📦 Complexity

| Type        | Value         |
|-------------|---------------|
| Time        | O(n²)         |
| Space       | O(log n) to O(n) depending on sort implementation |