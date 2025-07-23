# Container With Most Water

## Topic
- Array
- Two Pointers
- Greedy

---

## Problem
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are at `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container that holds the most water.

---

## Approach 1: Brute Force

- Try all pairs of lines `(left, right)` and compute the area.
- Track the maximum area found so far.

## Approach 2: Two Pointers

- Take two pointers left and right
- Compute the area for using both the pointers, shift the pointers left or right, based on the which is smaller, to get maximum area.

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |

---
## Test Cases

**Input**: height = [1,8,6,2,5,4,8,3,7]
**Output**: 49