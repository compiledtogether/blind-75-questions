# Longest Substring Without Repeating Characters

## Topic: String, Sliding Window

## Explanation


input: abcabcbb

output: 3

1. Take two pointers left and right
2. Slide the window to check the substring which has unique characters by using a set
3. If the set has already character, remove the left most character and increment the left pointer. why? if the first duplicate letter is found, no need to check the substring starting with first letter.
Start with immediate next from left letter.
4. calculate the result by checking max from result or (r-l + 1)