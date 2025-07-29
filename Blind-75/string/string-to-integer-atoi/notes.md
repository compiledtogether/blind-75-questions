# String to Integer (atoi)

## Topics
- String

---

## Explanation

### Algorithm

1. First strip down all the spaces from the string
2. Find out the sign in the beginning + or -, and store it in a variable
3. Iterate the rest of the string, convert individual character to string, after checking if it is digit
4. Include the digit in the result by adding, result = result * 10 + digit
5. After the loop, check if the result exceeds Max positive value and non negative, update result to max positive
6. If the result exceeds max negative value and negative, update the result to max negative
7. Lastly, return result, if sign is postive, else return result * -1

---

## Test Cases

**Input:** s = " -042"

**Output:** output = -42

--- 

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |
