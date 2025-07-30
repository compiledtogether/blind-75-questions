# Reverse Linked List

## Topics
- Linked List

---

## Explanation

### Algorithm

1. Initialize Pointers
- Take two pointers prev as None and curr as head

2. Loop Through Lists

- Iterate the list via curr
- Take a temp and assign curr to temp
- Assign curr.next to prev, i.e. reverse the pointers
- Assign curr to prev, i.e. move prev forward
- Assign temp to curr, i.e. move curr forward

3. Return the Result
return the prev, as it will new head of the list

---

## Test Cases

**Input:**
head = [1,2,3,4,5]
**Output:**
output = [5,4,3,2,1]

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(N)  |
| Space      | O(1)  |
