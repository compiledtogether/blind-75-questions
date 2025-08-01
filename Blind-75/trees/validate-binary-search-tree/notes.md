# Validate Binary Search Tree

## Topics
- Tree
- Recursion

---

## Explanation

### Algorithm

1. Base case:
- If root is none, return True

2. For each node, recursively compute:

- If node value lies between the low and high value, if not return False
- Else, call the helper function with left child, low, and node value
- and helper function with right child, node value and high value.

3. Initializer and return the helper function with root, negative infinity and positive infinity 


---

## Test Cases

**Input**
root = [5,1,4,None,None,3,6]
**Output**
output = False

---

## Time & Space Complexity

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

- **Time Complexity**: O(n)  
- **Space Complexity**: O(h), where h is the height of the tree.

---