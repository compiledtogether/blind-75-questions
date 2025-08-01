# Construct Binary Tree from Preorder and Inorder Traversal

## Topics
- Tree
- Recursion
- Hashing

---

## Explanation

### Algorithm

#### Approach 1: Recursion with List Slicing

1. The first element in the preorder list is always the root of the current subtree.

2. Find the index of the root in the inorder list.

3. The elements left of this index in inorder belong to the left subtree, and the elements right of it belong to the right subtree.

4. Slice the preorder list accordingly and recursively build left and right subtrees.

#### Approach 2: 

1. Build a hashmap to store the indices of inorder elements for O(1) lookup.

2. Use a shared pre_idx pointer to track the current root in preorder.

3. Use recursion with index boundaries instead of slicing.

4. This avoids list copying and gives an O(n) solution.

---

## Test Cases

### Test Case 1
**Input**:  
preorder = [3,9,20,15,7] 
inorder = [9,3,15,20,7]
**Output**:  
output = [3,9,20,None,None,15,7]

---


## Time & Space Complexity

1. Recursion and slicing

| Complexity | Value     |
|------------|-----------|
| Time       | O(n2)      |
| Space      | O(n2)      |

2. Hashmap and Recursion

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(n)      |