# Sqrt(x)

## Topics
- Math
- Binary Search

---

## Explanation

Use Binary search to find the sqrt of x

### Algorithm

1. Take left and right, 1 and x respectively, as the sqrt (floor integer) will be between 1 and x only
2. Iterate the loop, till left is smaller than equal to right.
3. Find mid, and calculate mid squared, if the mid squared is greater than x, update right to mid - 1
4. If the mid squared is smaller than x, update left to mid + 1 and update result to mid.
5. If mid sqaured is equal to x, then return mid.
6. If the loop breaks, return mid.

---

## Test Cases

**Input:** x = 8
**Output:** output = 2

--- 

## Time & Space Complexity

| Complexity | Value  |
|------------|--------|
| Time       | O(logn)|
| Space      | O(1)   |
