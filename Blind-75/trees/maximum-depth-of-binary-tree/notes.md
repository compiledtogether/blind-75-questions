# Maximum Depth of Binary Tree

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. If root is None, return 0
2. Else, calculate left depth using recursive call
3. calculate right depth using recursive call
4. return 1 + maximum of left depth or right depth

---

## Test Cases

**Input**
root = [3,9,20,None,None,15,7]
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
