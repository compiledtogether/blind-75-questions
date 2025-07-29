# Valid Parentheses

## Topics
- Stack
- String

---

## Explanation

#### Algorithm

1. Take stack and also create a dict with key as opening bracket and value as closing bracket
2. Iterate the string, if the character is opening bracket, add to the stack.
3. If they are not opening bracket, check if the Stack is empty or not, or closing bracket matches the corresponding opening bracket popped bracket from stack via dict
4. Return False, if the condition fails at any character
5. Lastly, check if the stack is empty or not, if yes, return true, else false.


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
