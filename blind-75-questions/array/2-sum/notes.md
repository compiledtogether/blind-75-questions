# Two Sum

## Topic
- Array
- Two Pointers

---

## Explanation

### Algorithm:

1. Create a hash map or dictionary.
2. Iterate through the array from the left, and for each value, calculate the complement as `(target - current value)`.
3. Check if the complement exists in the hash map:
   - If **yes**, return the pair of indices: `[complement_index, current_index]`.
   - If **no**, add the current value to the hash map with its index.
4. If no such pair is found after full traversal, return an empty array.

---

## 🧪 Test Cases

```python
nums1 = [2, 7, 11, 15]
target1 = 9
output1 = [0, 1]

nums2 = [3, 2, 4]
target2 = 6
output2 = [1, 2]

nums3 = [3, 3]
target3 = 6
output3 = [0, 1]
```

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |

## Note: If the numbers are sorted, then we can also use two pointer method, in which we can iterate from left and right, and try to find the sum, and move left or right, if the sum exceeds or falls short of the target.