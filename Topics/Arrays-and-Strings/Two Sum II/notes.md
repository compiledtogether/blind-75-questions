# Two Sum II

## Topic
- Array
- Two Pointers

---

## Explanation

### Algorithm:

1. Take two pointers, left and right
2. Iterate the loop till the time left is smaller than equal to right
3. Check if the sum of values at both the indices is equal to target or not, if yes, return [left+1, right+1]
4. If no, check if the sum is greater than target, decrement the right pointer
5. If the sum is smaller than target, increment the left pointer
6. If no result is return, return []

---

## Test Cases

```python
numbers = [2,7,11,15]
target = 9
Output= [1,2]
```

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |