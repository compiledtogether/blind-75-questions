# Jump Games

## Topics
- Array
- Greedy

---

## Explanation

Use greedy approach

### Algorithm

1. Tracks the farthest index we can currently reach.
2. Loop through each index to simulate walking from left to right.
3. If our current position i is beyond the maxReach, we are stuck.
4. This means we cannot reach this index, so we return False.
5. From the current position i, you can jump to i + nums[i].
6. Update maxReach to be the farthest we've seen so far.
7. If at any point, we can already reach or surpass the last index, we’re done.
8. Return True because reaching the end is possible.

---

## Test Cases

**Input:** nums = [2, 3, 1, 1, 4]
**Output**: True

**Input:** nums = [3, 2, 1, 0, 4]
**Output**: False

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |
