# Linked List Cycle

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

3. Return the Result
- Check if the slow and fast pointer are same, if yes, return true (cycle exists), else return false (no cycle) after loop ends.

---

## Test Cases

**Input:**
head = [3,2,0,-4]
**Output:**
output = True

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(N)  |
| Space      | O(N)  |
