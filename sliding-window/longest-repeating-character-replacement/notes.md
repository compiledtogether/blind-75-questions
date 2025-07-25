# Longest Repeating Character Replacement

## Topic
- String
- Sliding Window
- Hashing

---


## Explanation

### Approach: Using counter array and sliding window

### Algorithm:
1. Start with two pointers left and right for sliding window.
2. Create a empty 26 letter array initialized with 0 to count occurences.
3. Now, slide the window, by moving right pointer, and increment the occurenece, as we encounter each character.
4. After that, check if the difference between window length (r-l+1) and maximum of counts (number of occurences of each character) is greater than k, i.e. those many characters atleast needs change.
5. If the substring is found invalid, as per above condition (r-l+1 - max(counts)) > k, slide the window, by decrementing the occurence of character at left pointer, shift the left pointer to next character.
6. After the condition check, find the longest substring, by checking which is maximum, previously calculated longest or current window length.
7. Lastly return longest.

---

## Test Cases:

```python
s = "ABAB" 
k = 2
output = 4
```

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(n)  |