# Top K Frequent Elements

## Topic
- hashing
- array
- sorting

---

## Explanation

### Algorithm

1. Create a counter hashmap to count the frequency of the numbers from the list
2. Sort the hashmap in descending order of their frequency
3. Extract the k most frequent elements

---

## Test Cases

**Input:** nums, k = [1,1,1,2,2,3], 2
**Output**: output = [1,2]

---

## Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(nlogn)  |
| Space      | O(n)  |
