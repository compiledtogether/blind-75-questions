# Diameter of Binary Tree

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. For each node, recursively compute:

- left_height, right_height
- left_diameter, right_diameter

2. The diameter through the node is the sum of left and right subtree heights.

3. The final diameter is the maximum of:

- diameter through the current node
- left subtree's diameter
- right subtree's diameter

---

## Test Cases

**Input**
root = [1,2,3,4,5]
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
