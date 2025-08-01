# Kth Smallest Element in a BST

## Topics
- Tree
- Inorder

---

## Explanation

### Algorithm

1. Find the inorder traversal of the BST, and store it in a result list

2. Return the k - 1 index of the result, as the problem specifies 1-indexed tree.

---

## Test Cases

### Test Case 1
**Input**:  
root = [3,1,4,None,2]
k = 1
**Output**:  
output = 1

---


## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(h) for recursion stack (h = height of tree)