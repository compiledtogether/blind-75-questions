# Palindrome Linked List

## Topics
- Linked List
- Stack

---

## Explanation

### Approach 1: Using Stack

### Algorithm

1. Initialize Pointer and Stack
- Create a stack and dummy pointer 

2. Loop Through List

- Iterate the list via dummy pointer.
- Append all the elements of the list in the stack

3. Re-iterate list
- Loop through the same list again and pop from stack
- If the popped item and current value are equal, return False

3. Return the Result
Return True if stack is empty, else return False.

---

## Test Cases

**Input:**
head = [1,2,2,1]
**Output:**
output = True

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(N)  |
| Space      | O(N)  |
