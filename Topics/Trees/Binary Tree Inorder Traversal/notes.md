# Binary Tree InOrder Traversal

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. Take a result empty array
2. Create a helper function, which will be used for recursive call for traversal.
3. Check if root is None, return
4. Else, First make recursive call to left child 
5. Then, append the root value to the result and then make recursive call to right child
6. Outside of the helper function call, make the initial call to the helper function as root
7. Return the result array, as it will have the desired output


---

## Test Cases

### Test Case 1
**Input**:  
root = [1,2,3,4,5,None,8,None,None,6,7,9]
**Output**:  
output = [4,2,6,5,7,1,3,9,8]

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(h) for recursion stack (h = height of tree)