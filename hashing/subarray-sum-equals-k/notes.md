# Subarray Sum Equals K

## Topics
- Array
- Hashing
- prefix sum

---

## Explanation

If `currSum` is the sum of elements from 0 to i, and we know there was a previous prefixSum of `currSum - k`, then the subarray between that previous prefix and the current position must sum to k.

### Algorithm
For every number in the array:

1. Add the number to currSum.

2. Compute diffSum = currSum - k.

3. If diffSum exists in prefixSum, it means there is a subarray ending at current index with sum = k → add its count to result.

4. Update the frequency of currSum in prefixSum.

--- 

## Test Cases

**Input:**
nums = [1,1,1]
k = 2
**Output:**
Output= 2
---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |