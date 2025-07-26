# Pow(x,n)

## Topics
- Math
- Recursion

---

## Explanation

### Approach 1: Brute Force

### Algorithm

1. Iterate a loop n times, and multiply x with it, res *= x
2. Return res, after loop ends

### Approach 2: Recursion

### Algorithm

1. Create helper function
2. Take base case, if n is 0, return 1, if x is 0, return 0
3. Calculate pow, by doing n // 2, and calling helper recursively and store in res, 
4. After res is calculated, multiple it with itself, to get actual value
5. If n is odd, multiply one more time x with the result, else return res as it is.
6. Call this helper from main function with absolute value of n
7. If n is negative, return 1 / res, else, return res as it is.

---

## Test Cases

**Input:** 
x = 2
n = 10
**Output:** 
output = 1024

--- 

## Time & Space Complexity

| Complexity | Value  |
|------------|--------|
| Time       | O(logn)|
| Space      | O(1)   |
