# Merge K sorted lists

## Topics
- Linked List
- Divide and Conquer

---

## Explanation

### Algorithm

1. Define mergeTwoLists

    Use the algorithm from merging two lists

    1. Initialize Result List
    - Initialize a new list, named result, and create a temp pointer for iterating the result list

    2. Loop Through Lists

    - Iterate the two list together, as any of them can be a sorted list 
    - Check if the value of list1 is smaller than list2 value, whichever is smaller, attach that to the result.next and increment it
    - Move result forward

    3. Attach remaining list
    - Check whichever list is remaining and attach the remaining to the result.next

    4. Return the Result
    return the resultHead.next, as it points to the head of result

2. Define divideAndConquer

- Create a divideAndConquer function which accepts lists, left and right pointer
- If left and right are same return lists[left] (any of the list)
- find mid value of from left and right
- l1 = divideAndConquer(lists, left, mid)
- l2 = divideAndConquer(lists, mid + 1, right)
- return mergeTwoLists(l1, l2)

3. Call divideAndConquer

- Add a base condition, if the lists is none, return none
- From actual function call this divideAndConquer function with parameters as lists, 0 (left most) and len(lists) - 1 (right most), returns the result from this function



---

## Test Cases

**Input:**
list1 = [[1,4,5],[1,3,4],[2,6]]
**Output:**
output = [1,1,2,3,4,4,5,6]

--- 

## Time & Space Complexity

| Complexity | Value      |
|------------|------------|
| Time       | O(N log k) |
| Space      | O(log k)   |

Time Complexity: O(N log k)
( N ): Total number of nodes across all lists.
( log k ): Number of levels in the divide-and-conquer recursion tree.
Space Complexity: O(log k) due to recursive function calls.