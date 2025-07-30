# Add Two Numbers

## Topics
- Linked List

---

## Explanation

### Algorithm

1. Initialize Pointers
- dummy is a placeholder node to start building the result linked list.
- current is a pointer to the current position in the result list.
- carry holds the carry-over value from each digit addition (e.g., 7 + 5 = 12 → carry = 1).

2. Loop Through Lists

This loop continues as long as there's something to add — either:

- more digits in l1
- more digits in l2
- or a carry left from the last addition.

3. Add Corresponding Digits and Carry

- Start with the carry from the last iteration.
- Add the current digit from l1 and move l1 forward.
- Do the same for l2.

4. Compute New Digit and Carry
- sum // 10 gives the new carry (e.g., if sum is 17 → carry = 1).
- sum % 10 is the digit to store in the result list (e.g., 17 → store 7).
- Move the current pointer to the newly added node.

5. Return the Result
dummy.next points to the head of the new linked list (we skip the dummy node itself).

---

## Test Cases

**Input:**
l1 = [2,4,3]
l2 = [5,6,4]
**Output:**
Output: [7,0,8]

--- 

## Time & Space Complexity

| Complexity | Value        |
|------------|--------------|
| Time       | O(max(N, M)) |
| Space      | O(max(N, M)) |
