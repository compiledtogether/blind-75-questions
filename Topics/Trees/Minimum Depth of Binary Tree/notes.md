# Minimum Depth of Binary Tree

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. If root is None, return 0
2. If left child is not present, make recursive call with right child and return result + 1
3. If right child is not present, make recursive call with left child and return result + 1
4. Finally, return 1 + minimum of left depth and right depth

---

## Test Cases

**Input**
root = [3,9,20,None,None,15,7]
**Output**
output = 2

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(h), where h is the height of the tree.

---
