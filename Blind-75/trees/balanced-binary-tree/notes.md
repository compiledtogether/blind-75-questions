# Balanced Binary Tree

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. For each node, recursively compute:

- left_height, right_height
- left_balanced, right_balanced

2. The isBalanced for a node is if it's all the left child and right child are balanced and abs(left_height - right_height) is less than equal to 1

3. The final result will be:
- isBalanced result for the root


---

## Test Cases

**Input**
root = [3,9,20,None,None,15,7]
**Output**
output = True

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(h), where h is the height of the tree.

---
