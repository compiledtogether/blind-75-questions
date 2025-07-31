# Binary Tree Level Order Traversal

## Topics
- Tree
- Breadth-First Search (BFS)
- Queue

---

## Explanation

### Algorithm

The level order traversal of a binary tree visits nodes level by level from left to right. This is achieved using a **Breadth-First Search (BFS)** approach.

1. **Base Case**: If the tree is empty (root is `None`), return an empty list.
2. **Initialize Queue**: Use a queue (FIFO) to hold nodes at each level. Start with the root node.
3. **While the queue is not empty**:
   - For each node at the current level (length of the queue):
     - Dequeue it, record its value.
     - Enqueue its left and right children if they exist.
   - Append the collected values for this level to the result list.
4. Return the `result` list which contains a list of values at each level.

This algorithm ensures each level of the tree is visited once, and all nodes are processed in order.

---

## Test Cases

### Test Case 1
**Input**:  
`[3, 9, 20, None, None, 15, 7]`  
**Output**:  
`[[3], [9, 20], [15, 7]]`

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(n)      |

- **Time Complexity**: `O(n)` where `n` is the number of nodes in the tree. Each node is visited once.
- **Space Complexity**: `O(n)` for the queue in the worst case (when the bottom level is full).