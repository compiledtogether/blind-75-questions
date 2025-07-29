# Middle of the Linked List

## Topics
- Linked List

---

## Explanation

### Algorithm

1. Initialize Pointers
- Take two pointers first and second

2. Loop Through Lists

- Iterate the list via second pointer, check till the second pointer reaches last node.
- Increment first pointer to next node
- Increment second pointer to next to next node

Note: One pointer will move one step and another one will move two steps

3. Return the Result
return the first pointer, as it will reach the middle of the list

---

## Test Cases

**Input:**
head = [1,2,3,4,5]
**Output:**
output = [3,4,5]

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(N)  |
| Space      | O(N)  |
