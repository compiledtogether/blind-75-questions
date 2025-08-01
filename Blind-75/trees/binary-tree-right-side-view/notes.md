# Binary Tree Right Side View

## Topics
- Tree
- Breadth-First Search (BFS)
- Queue

---

## Explanation

### Algorithm

1. Initialize:
- Create an empty list result to store the result (rightmost values at each level).
- Create a queue q using deque() for BFS traversal.
- Add the root node to the queue.


2. Start BFS Loop:
- While the queue is not empty:
- Set a placeholder right_side = None to keep track of the last non-null node at the current level.

3. Process One Level at a Time:
- For every node in the current level (determined by len(q)):
- Remove (popleft) a node from the front of the queue.
- If the node is not None:
    - Update right_side to this node (we're scanning left → right, so the last - non-null node is the rightmost one).
    - Add the node’s left and right children to the queue (even if they are None).


4. After the Level is Processed:
If right_side is not None, add its value to the result list.

5. Repeat:
Go back to Step 2 until the queue is empty.

6. Return the Result:
return result

---

## Test Cases

### Test Case 1
**Input**:  
root = [1,2,3,None,5,None,4]
**Output**:  
output = [1,3,4] 

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(n)      |