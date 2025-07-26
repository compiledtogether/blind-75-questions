# Permutation in Strings

## Topic
- String
- Sliding Window
- Hashing

---


## Explanation

### Algorithm:

### Approach 1: using hashmap

The sliding window technique allows us to efficiently compare character frequencies in substrings of s2 with s1. Here's the approach:

1. Use a dictionary to count character frequencies for s1.
2. Maintain a window of size len(s1) on s2 and keep track of character frequencies in that window.
2. Slide the window across s2, updating the character counts and comparing them to s1's counts.

### Approach 2: without hashmap

1. Frequency Array Initialization:

- We create two frequency arrays of size 26, one for s1 and one for s2. Each index of the array corresponds to a letter in the alphabet.
- We populate the arrays with the character counts of s1 and the first window in s2 (of size s1.length()).

2. Sliding Window:

- We start with the first window in s2 and slide it over the string.
- For each slide, we remove the frequency count of the character that’s leaving the window and add the frequency count of the new character entering the window.

3. Frequency Comparison:

- At each step of the sliding window, we compare the frequency arrays of the current window and s1. If they match, we know that the window is a permutation of s1.

4. Return Result:

- If we find a matching window, we return true.
- If no matching window is found after sliding through all of s2, we return false.
---

## Test Cases:

```python
s1 = "ab"
s2 = "eidbaooo"
output = True
```

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(26) ~ O(1)  |