# Jump Games II

## Topics
- Array
- Greedy

---

## Explanation

Use greedy approach

### Algorithm

1. We don't need to jump from last index, so, run the loop till second last (n-2)th index
2. At each step, calculate the farthest index, we can reach from current range, farthest = max(farthest, i + nums[i])
3. If we've reached, the end of the current jump range, i.e. i == current, so, we make the jump now, and update
jumps and current to farthest.
4. Lastly return the jumps

---

## Test Cases

**Input:** 
nums = [2,3,1,1,4]

**Output:** 
Output: 2

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |
