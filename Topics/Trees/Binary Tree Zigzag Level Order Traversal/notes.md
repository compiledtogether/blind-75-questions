# Binary Tree Zigzag Level Order Traversal

## Topics
- Tree
- Breadth-First Search (BFS)
- Queue

---

## Explanation

### Algorithm

This problem is a variation of standard level order traversal (BFS), where we print the nodes at each level in **alternating left-to-right and right-to-left order** — also known as *zigzag* traversal.

1. **Base Case**: If the root is `None`, return an empty list.
2. **Initialize**:
   - A queue (`deque`) to perform BFS starting from the root.
   - A boolean flag `reverse` to track the direction of traversal at each level.
3. **While the queue is not empty**:
   - Create a list `level` to store the current level's node values.
   - For each node in the current level:
     - If `reverse` is `False`, pop nodes from the left side of the queue (standard BFS).
       - Append children in order: left, then right.
     - If `reverse` is `True`, pop nodes from the right side of the queue.
       - Append children in reverse order: right, then left **to the front of the queue** to maintain order.
   - After processing the level, append `level` to the result list.
   - Flip the `reverse` flag for the next level.

---

## Test Cases

### Test Case 1
**Input**:  
`[3, 9, 20, None, None, 15, 7]`  
**Output**:  
`[[3],[20,9],[15,7]]`

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(n)      |

- **Time Complexity**: `O(n)` where `n` is the number of nodes in the tree. Each node is visited once.
- **Space Complexity**: `O(n)` for the queue in the worst case (when the bottom level is full).