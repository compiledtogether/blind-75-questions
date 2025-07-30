# Reverse Nodes in K Group

## Topics
- Linked List

---

## Explanation

### Approach 1: Recursive

### Algorithm

1. Check if we need to reverse the group
2. Reverse the group, normal reverse linked list algorith,
3. After reverse, head is the tail of the group and curr is the next pointer in original linked list
4. Update head.next to the recursive call to the function with curr and k
5. Return prev

### Approach 2: Iterative

### Algorithm

1. Check if there is no node in head or k is 1, return head
2. create a new dummy node, and put head to the dummy.next 
3. initialize prev as dummy and curr as head
4. count number of the nodes in the list
5. reverse k nodes at a time, by iterating till count >= k
6. Forward curr and nxt node
7. Reverse k nodes at a time, use curr and nxt and prev for reversing
8. Update prev to curr
9. decrement count by k
10. return dummy.next

---

## Test Cases

**Input:**
head = [1,2,3,4,5]
k = 2
**Output:**
output = [2,1,4,3,5]

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(N)  |
| Space      | O(1)  |
