# Maximum Depth of n-ary Tree

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. If root is None, return 0
2. Iterate all the children of the root
3. Find max depth for the children by comparing current max and recursive call
4. return 1 + max depth

---

## Test Cases

**Input**
root = [1,None,3,2,4,None,5,6]
**Output**
output = 3

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(h), where h is the height of the tree.

---
