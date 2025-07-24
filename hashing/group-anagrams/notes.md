# Group Anagrams

## Topics
- Hashing

---

## Explanation

### Algorithm

1. Create a hash map to store the sorted value of each string
2. If the sorted value of each string is present, append the string to the value list for the key
3. Else, create a new list with the string
4. Return the list of values in a result variable

---

## Test Cases

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** Output = [["bat"],["nat","tan"],["ate","eat","tea"]]

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(k*nlong)  |
| Space      | O(k*n)  |



