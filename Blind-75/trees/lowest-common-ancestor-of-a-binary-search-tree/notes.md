# Lowest Common Ancestor of a Binary Search Tree

## Topics
- Tree
- Recursion
- Divide and Conquer

---

## Explanation

### Algorithm

The goal is to find the **lowest common ancestor (LCA)** of two nodes `p` and `q` in a binary tree.

1. **Base Case**:
   - If the current node `root` is `None`, or equals `p` or `q`, return `root`.
   - This means either we’ve reached the end of a path, or found one of the nodes.

2. **Recursive Calls**:
   - Recursively call on the left and right subtree.
   - Store the result in `left` and `right`.

3. **Decision**:
   - If both `left` and `right` are non-null, it means `p` and `q` are found in different subtrees — so `root` is their LCA.
   - If only one is non-null, return the non-null one — it's either `p` or `q`, or their ancestor.
   - If both are `None`, return `None`.

This approach works because it bubbles up the found node and identifies the split point where the nodes diverge.

---

## Test Cases

**Tree Input**:  
`[6,2,8,0,4,7,9,None,None,3,5]`
**p = 2, q = 8**

**Output**: `6`

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n) — in the worst case, we visit all `n` nodes.
- **Space Complexity**: O(h) — where `h` is the height of the tree (recursion stack).

---
