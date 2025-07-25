# Longest Substring Without Repeating Characters

## Topic
- String
- Sliding Window

---


## Explanation

### Algorithm:
1. Take two pointers `left` and `right`.
2. Slide the window using a set to track unique characters.
3. If the set already contains the character at `right`, remove the leftmost character and increment `left`.  
   - Why? Because once a duplicate is found, there's no point in checking substrings starting with the current `left`—move to the next character.
4. Update the result as the maximum of the current result and `(right - left + 1)`.

---

## Test Cases:

```python
string = 'abcabcbb'  
output = 3
```

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |