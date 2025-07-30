# LRU Cache

## Topics
- Linked List
- Doubly Linked List
- LRU
- Hashing

---

## Explanation

### Approach 1: Using OrderedDict

### Algorithm

1. Create cache as OrderedDict
2. In get function, if the item is present, return it, but before move the item to end
3. In put function, if the item is present, move item to end, else, add the key and value to cache.
4. After adding, check if the cache size is greater than capacity or not, if yes, remove the initial item from head.


---

## Test Cases

**Input:**
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
**Output:**
[null, null, null, 1, null, -1, null, -1, 3, 4]

--- 

## Time & Space Complexity

1. get()
| Complexity | Value |
|------------|-------|
| Time       | O(1)  |
| Space      | O(N)  |

2. put()
| Complexity | Value |
|------------|-------|
| Time       | O(1)  |
| Space      | O(N)  |
