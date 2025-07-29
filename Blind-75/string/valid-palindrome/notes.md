# Valid Palindrome

## Topics
- Two Pointers
- String

---

## Explanation

### Approach 1: Two Pointers

#### Algorithm

1. Take two pointers, left and right.
2. Run the loop till left is smaller than right
3. If there is any non-alphanumeric, increment the left or decrement the right
4. Compare the two pointers, if at any point, they are not equal return False
5. Finally, return True

### Approach 2: Without Two pointers

#### Algorithm:

1. Strip down the spaces from the string, convert every letter to lowercase
2. Reverse the string and compare with the clean string
3. Return True, if they are equal, else False.


---

## Test Cases

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** True

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |
