# Merge two sorted lists

## Topics
- Linked List

---

## Explanation

### Algorithm

1. Initialize Result List
- Initialize a new list, named result, and create a temp pointer for iterating the result list

2. Loop Through Lists

- Iterate the two list together, as any of them can be a sorted list 
- Check if the value of list1 is smaller than list2 value, whichever is smaller, attach that to the result.next and increment it
- Move result forward

3. Attach remaining list
- Check whichever list is remaining and attach the remaining to the result.next


3. Return the Result
return the resultHead.next, as it points to the head of result

---

## Test Cases

**Input:**
list1 = [1,2,4]
list2 = [1,3,4]
**Output:**
output = [1,1,2,3,4,4]

--- 

## Time & Space Complexity

| Complexity | Value       |
|------------|-------------|
| Time       | O(MIN(N,M)) |
| Space      | O(N+M)      |
