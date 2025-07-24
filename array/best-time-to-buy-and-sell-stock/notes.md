# Best Time to Buy and Sell Stock

## Topics
- Array

---

## Explanation

Iterate the elements, start for minimal value for buy, so that, profit can be maximized on the day of sell.

### Algorithm

#### Approach 1: (Using Set)

1. Initialize buy with first day value, and profit as 0
2. Iterate from day 2 value to last day, if the buy value is greater, update the buy value, else, find the profit for that day, and if the profit (current day - buy day) is greater, update the profit.
3. Return the profit

--- 

## Test Cases

**Input:**
prices1 = [7,1,5,3,6,4]
**Output:**
output1 = 5

**Input:**
prices2 = [7,6,4,3,1]
**Output:**
output2 = 0

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |