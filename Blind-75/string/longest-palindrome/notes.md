# Longest Palindrome

## Topics
- Hashing
- String

---

## Explanation

#### Algorithm

1. Create a counter hashmap, where count of each character is stored as value and key as character
2. Iterate the hashmap, if the value of the key is even, add the value to count variable
3. If the value of the key is odd, add value - 1 to count variable, flip the flag to true, to track that we have odd value item
4. Finally, return the value of count, if the flag is false, else return count + 1


---

## Test Cases

**Input:** s = "()[]{}"
**Output:** True

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |
