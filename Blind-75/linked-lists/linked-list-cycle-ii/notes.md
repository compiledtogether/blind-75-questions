# Linked List Cycle II

## Topics
- Linked List

---

## Explanation

### Algorithm

1. Initialize Pointers
- Take two pointers fast and slow

2. Loop Through Lists

- Iterate the list via second pointer, check till the second pointer reaches last node.
- Increment first pointer to next node
- Increment second pointer to next to next node

Note: One pointer will move one step and another one will move two steps

3. Detect loop
- Check if the slow and fast pointer are same, if yes, break the loop (cycle exists), else return None (no cycle) after loop ends.

4. Re-initialize the fast pointer
- Re-initialize the fast pointer to head, and run the loop till the fast and slow pointer are not same. By incrementing the slow and fast pointer together

5. Return the result:
- Once the loop breaks, return the slow pointer

---

## Test Cases

**Input:**
head = [3,2,0,-4]
pos = 1
**Output:**
Output = "tail connects to node index 1"

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(N)  |
| Space      | O(N)  |
