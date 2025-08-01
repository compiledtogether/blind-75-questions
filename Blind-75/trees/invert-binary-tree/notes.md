# Invert Binary Tree

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. Check if the root is None. If it is, return None. This is the base case for the recursion, which handles empty subtrees.

2. Swap Left and Right Children
- Store the left child of the current node (root.left) in a temporary variable temp.
- Assign the right child of the current node (root.right) to the left child (root.left).
- Assign the value stored in temp (original left child) to the right child (root.right).
- This effectively swaps the left and right children of the current node.

3. Recursively call invertTree on the left child of the current node. Since we have swapped the children, this call will actually invert the original right subtree.
4. Recursively call invertTree on the right child of the current node. Since we have swapped the children, this call will actually invert the original left subtree.
5. Return root


---

## Test Cases

**Input**
root = [4,2,7,1,3,6,9]
**Output**
output = [4,7,2,9,6,3,1]

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(n)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(n)

---
