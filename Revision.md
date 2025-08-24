<!-- # 📘 Last-Minute DSA Revision Notes

---

## 1. Trapping Rain Water (H)
- **Pattern**: Array, Two-Pointer, Prefix/Suffix  
- **Approach**:  
  - Precompute `leftMax` and `rightMax` for each bar.  
  - Optimized two-pointer: track `leftMax` & `rightMax` and calculate trapped water.  
- **Time**: O(n), **Space**: O(1) / O(n).  
- **Pointers**:  
  - Prefix/suffix maxima simplify.  
  - Related: Container With Most Water, Histogram problems.  

---

## 2. Alien Dictionary (Foreign Dictionary / Order of Characters)
- **Pattern**: Graph, Topological Sort  
- **Approach**:  
  - Build graph from word differences.  
  - Perform topo sort, detect cycles.  
- **Time**: O(V+E), **Space**: O(V+E).  
- **Pointers**:  
  - Handle prefix conflicts (`["abc","ab"]` invalid).  
  - Similar: Course Schedule, Task Scheduling.  

---

## 3. Partition Equal Subset Sum
- **Pattern**: DP, Subset-Sum  
- **Approach**:  
  - Check if `sum` is even.  
  - Use DP to check subset with `sum/2`.  
- **Time**: O(n*sum), **Space**: O(sum).  
- **Pointers**:  
  - Classic subset/knapsack.  
  - Think “subset existence” for variations.  

---

## 4. Median of Two Sorted Arrays (H)
- **Pattern**: Binary Search  
- **Approach**:  
  - Binary search on smaller array partitions.  
  - Median = `max(left) + min(right)`.  
- **Time**: O(log(min(n,m))), **Space**: O(1).  
- **Pointers**:  
  - Useful in kth-element problems.  
  - Edge cases: empty arrays, uneven partition.  

---

## 5. Task Scheduler
- **Pattern**: Greedy + Heap  
- **Approach**:  
  - Use max-heap of task frequencies.  
  - Formula: `max((maxFreq-1)*(n+1)+countMaxFreq, totalTasks)`.  
- **Time**: O(n), **Space**: O(1)/O(26).  
- **Pointers**:  
  - Cooldown/interval → greedy/formula.  

---

## 6. Gas Station
- **Pattern**: Greedy  
- **Approach**:  
  - If total gas < cost → impossible.  
  - Traverse, reset start if balance < 0.  
- **Time**: O(n), **Space**: O(1).  
- **Pointers**:  
  - Reset trick useful in circular route problems.  

---

## 7. Contiguous Array (Equal 0s and 1s)
- **Pattern**: Prefix Sum + HashMap  
- **Approach**:  
  - Replace 0 → -1.  
  - Track prefix sum, store earliest index.  
- **Time**: O(n), **Space**: O(n).  
- **Pointers**:  
  - Equal count → prefix sum trick.  

---

## 8. Counting Bits
- **Pattern**: DP on Bits  
- **Approach**:  
  - Relation: `dp[i] = dp[i>>1] + (i&1)`.  
- **Time**: O(n), **Space**: O(n).  
- **Pointers**:  
  - Bit DP: shift (`>>1`), lowest set bit (`i&(i-1)`).  

---

## 9. Next Greater Element I
- **Pattern**: Monotonic Stack  
- **Approach**:  
  - Traverse from right.  
  - Decreasing stack, top is next greater.  
- **Time**: O(n), **Space**: O(n).  
- **Pointers**:  
  - Next greater/smaller → monotonic stack.  

---

## 10. Range Sum Query (Immutable)
- **Pattern**: Prefix Sum  
- **Approach**:  
  - Precompute prefix array.  
  - Query: `prefix[j+1]-prefix[i]`.  
- **Time**: O(n+q), **Space**: O(n).  
- **Pointers**:  
  - Static sums → prefix sum.  

---

## 11. Word Search II
- **Pattern**: Backtracking + Trie  
- **Approach**:  
  - Insert words into Trie.  
  - DFS grid, prune invalid prefixes.  
- **Time**: O(N * 4^L) worst.  
- **Pointers**:  
  - Combine Trie + DFS when searching multiple words.  

---

## 12. Burst Balloons (H)
- **Pattern**: Interval DP  
- **Approach**:  
  - Recurrence: `dp[i][j] = max(dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])`.  
- **Time**: O(n^3), **Space**: O(n^2).  
- **Pointers**:  
  - Interval DP = choose “last” element inside.  
  - Related: Matrix Chain Multiplication.  

---

## 13. LRU Cache
- **Pattern**: HashMap + Doubly Linked List  
- **Approach**:  
  - DLL for order, HashMap for O(1) access.  
  - On get/put, move node to head.  
- **Time**: O(1), **Space**: O(capacity).  
- **Pointers**:  
  - Cache design → HashMap + DLL.  

---

# 📘 Last-Minute DSA Revision Notes (Collapsible Cheat Sheet)

---

## Arrays & Sliding Window

<details>
<summary>Sliding Window Maximum</summary>

- **Pattern**: Monotonic Deque  
- **Approach**: Maintain deque of indices, pop smaller elements, front is max.  
- **Time**: O(n), **Space**: O(k).  
- **Pointers**: Sliding window min/max → deque.  

</details>

<details>
<summary>Trapping Rain Water (H)</summary>

- **Pattern**: Two-Pointer / Prefix-Suffix  
- **Approach**: Track leftMax & rightMax, accumulate water.  
- **Time**: O(n), **Space**: O(1).  
- **Pointers**: Similar to Container with Water, Histogram.  

</details>

<details>
<summary>Maximum Subarray</summary>

- **Pattern**: Kadane’s Algorithm  
- **Approach**: Track `maxEndingHere`, update global max.  
- **Time**: O(n), **Space**: O(1).  

</details>

<details>
<summary>Maximum Product Subarray</summary>

- **Pattern**: DP with min/max  
- **Approach**: Track `minProd` and `maxProd` because of negatives.  
- **Time**: O(n), **Space**: O(1).  

</details>

<details>
<summary>Product of Array Except Self</summary>

- **Pattern**: Prefix + Suffix products  
- **Approach**: Multiply left product and right product arrays.  
- **Time**: O(n), **Space**: O(1) extra.  

</details>

<details>
<summary>Container With Most Water</summary>

- **Pattern**: Two-pointer  
- **Approach**: Start ends, move smaller height inward.  
- **Time**: O(n).  

</details>

<details>
<summary>Jump Game</summary>

- **Pattern**: Greedy  
- **Approach**: Track farthest reachable index.  
- **Time**: O(n).  

</details>

<details>
<summary>Jump Game II</summary>

- **Pattern**: Greedy BFS-like  
- **Approach**: Track current jump range & increment when exceeded.  
- **Time**: O(n).  

</details>

<details>
<summary>Best Time to Buy and Sell Stock</summary>

- **Pattern**: Greedy  
- **Approach**: Track min price so far, compute max profit.  
- **Time**: O(n).  

</details>

---

## Prefix Sum / HashMap

<details>
<summary>Contiguous Array</summary>

- **Pattern**: Prefix Sum + HashMap  
- **Approach**: Replace 0 → -1, use prefix sum difference.  
- **Time**: O(n).  

</details>

<details>
<summary>Subarray Sum Equals K</summary>

- **Pattern**: Prefix Sum + HashMap  
- **Approach**: Count prefix[j]-prefix[i]=k with HashMap freq.  
- **Time**: O(n).  

</details>

<details>
<summary>Range Sum Query (Immutable)</summary>

- **Pattern**: Prefix Sum  
- **Approach**: Precompute prefix array, query in O(1).  
- **Time**: O(n+q).  

</details>

---

## Graph / BFS / DFS

<details>
<summary>Number of Islands</summary>

- **Pattern**: DFS/BFS/Union-Find  
- **Approach**: Flood fill count components.  
- **Time**: O(n*m).  

</details>

<details>
<summary>Number of Provinces</summary>

- **Pattern**: DFS / Union-Find  
- **Approach**: Count connected components in adjacency matrix.  

</details>

<details>
<summary>Course Schedule</summary>

- **Pattern**: Graph Topological Sort  
- **Approach**: Detect cycle via DFS/Kahn’s algo.  

</details>

<details>
<summary>Course Schedule II</summary>

- **Pattern**: Graph Topological Sort  
- **Approach**: Kahn’s algo gives valid order.  

</details>

<details>
<summary>Word Ladder</summary>

- **Pattern**: BFS shortest path  
- **Approach**: Transform by changing 1 letter, BFS levels.  

</details>

<details>
<summary>Alien Dictionary</summary>

- **Pattern**: Graph Topo Sort  
- **Approach**: Build graph from words, topo sort.  

</details>

<details>
<summary>Is Bipartite</summary>

- **Pattern**: Graph Coloring BFS/DFS  
- **Approach**: 2-coloring, detect conflicts.  

</details>

<details>
<summary>Clone Graph</summary>

- **Pattern**: DFS/BFS + HashMap  
- **Approach**: Map old → new node while traversing.  

</details>

<details>
<summary>Find if Path Exists in Graph</summary>

- **Pattern**: BFS/DFS connectivity  
- **Approach**: Explore graph, check reachability.  

</details>

<details>
<summary>Region Cut by Slashes</summary>

- **Pattern**: Union-Find  
- **Approach**: Divide each cell into 4 triangles, union them.  

</details>

<details>
<summary>Number of Closed Islands</summary>

- **Pattern**: DFS on grid  
- **Approach**: Flood-fill border zeros, count remaining.  

</details>

<details>
<summary>Surrounded Regions</summary>

- **Pattern**: DFS/BFS  
- **Approach**: Mark border 'O's, flip rest.  

</details>

<details>
<summary>01 Matrix</summary>

- **Pattern**: BFS multi-source  
- **Approach**: Start BFS from 0s, fill distances.  

</details>

<details>
<summary>Rotten Oranges</summary>

- **Pattern**: BFS multi-source  
- **Approach**: Push all rotten initially, BFS level = minutes.  

</details>

<details>
<summary>Flood Fill</summary>

- **Pattern**: DFS/BFS  
- **Approach**: Recursively recolor connected component.  

</details>

---

## Binary Tree & BST

<details>
<summary>Binary Tree Right Side View</summary>

- **Pattern**: BFS  
- **Approach**: Take last node at each level.  

</details>

<details>
<summary>LCA Binary Tree</summary>

- **Pattern**: DFS recursion  
- **Approach**: Return node if found, else combine results.  

</details>

<details>
<summary>LCA BST</summary>

- **Pattern**: BST property  
- **Approach**: Traverse until split point.  

</details>

<details>
<summary>Balanced Binary Tree</summary>

- **Pattern**: DFS post-order  
- **Approach**: Return -1 if imbalance found.  

</details>

<details>
<summary>Diameter of Binary Tree</summary>

- **Pattern**: DFS  
- **Approach**: Max path = leftHeight+rightHeight.  

</details>

<details>
<summary>Invert Binary Tree</summary>

- **Pattern**: DFS recursion  
- **Approach**: Swap children.  

</details>

<details>
<summary>Kth Smallest in BST</summary>

- **Pattern**: Inorder traversal  
- **Approach**: Stop at kth element.  

</details>

<details>
<summary>Validate BST</summary>

- **Pattern**: DFS with bounds  
- **Approach**: Check node.val ∈ (low, high).  

</details>

<details>
<summary>Construct Binary Tree from Pre/Inorder</summary>

- **Pattern**: Recursion  
- **Approach**: Root from preorder, split inorder via hashmap.  

</details>

---

## Linked List

<details>
<summary>Linked List Cycle</summary>

- **Pattern**: Two-pointers  
- **Approach**: Detect cycle with fast/slow.  

</details>

<details>
<summary>Linked List Cycle II</summary>

- **Pattern**: Floyd’s cycle  
- **Approach**: Reset pointer to head after meeting point.  

</details>

<details>
<summary>Middle of the Linked List</summary>

- **Pattern**: Two-pointer  
- **Approach**: Fast moves 2x.  

</details>

<details>
<summary>Add Two Numbers</summary>

- **Pattern**: Linked List digit addition  
- **Approach**: Add digits with carry.  

</details>

<details>
<summary>Merge k Sorted Lists</summary>

- **Pattern**: Heap / Divide-Conquer  
- **Approach**: Min-heap or merge pairs recursively.  

</details>

<details>
<summary>Reverse Nodes in k-Group</summary>

- **Pattern**: Linked List manipulation  
- **Approach**: Reverse sublist of k nodes iteratively.  

</details>

<details>
<summary>LRU Cache</summary>

- **Pattern**: HashMap + DLL  
- **Approach**: O(1) get/put, maintain DLL order.  

</details>

---

## Strings

<details>
<summary>Minimum Window Substring</summary>

- **Pattern**: Sliding Window  
- **Approach**: Expand until valid, shrink while valid.  

</details>

<details>
<summary>Permutation in String</summary>

- **Pattern**: Sliding Window  
- **Approach**: Compare window freq with target freq.  

</details>

<details>
<summary>Longest Repeating Character Replacement</summary>

- **Pattern**: Sliding Window  
- **Approach**: Expand while `windowLen - maxFreq <= k`.  

</details>

<details>
<summary>Longest Substring Without Repeating Characters</summary>

- **Pattern**: Sliding Window  
- **Approach**: Expand, shrink if duplicate.  

</details>

<details>
<summary>Valid Palindrome</summary>

- **Pattern**: Two-pointer  
- **Approach**: Ignore non-alphanum, compare ends.  

</details>

<details>
<summary>Valid Anagram</summary>

- **Pattern**: HashMap / Sorting  
- **Approach**: Count characters or sort & compare.  

</details>

<details>
<summary>Valid Parentheses</summary>

- **Pattern**: Stack  
- **Approach**: Push opening, pop matching closing.  

</details>

<details>
<summary>Longest Palindrome</summary>

- **Pattern**: HashMap freq  
- **Approach**: Use even counts, at most one odd.  

</details>

<details>
<summary>String to Integer (atoi)</summary>

- **Pattern**: Parsing  
- **Approach**: Trim spaces, handle sign, parse digits.  

</details>

<details>
<summary>Rearrange Spaces Between Words</summary>

- **Pattern**: String Manipulation  
- **Approach**: Distribute spaces evenly, leftover at end.  

</details>

---

## Heaps / Priority Queue

<details>
<summary>Kth Largest Element in Stream</summary>

- **Pattern**: Min-Heap  
- **Approach**: Keep heap of size k.  

</details>

<details>
<summary>Top K Frequent Elements</summary>

- **Pattern**: Heap / Bucket Sort  
- **Approach**: Count frequencies, extract top k.  

</details>

---

## Math / Bit Manipulation

<details>
<summary>Single Number</summary>

- **Pattern**: XOR  
- **Approach**: XOR cancels duplicates.  

</details>

<details>
<summary>Missing Number</summary>

- **Pattern**: XOR / Sum  
- **Approach**: XOR 0..n with nums, or sum formula.  

</details>

<details>
<summary>Counting Bits</summary>

- **Pattern**: DP bits  
- **Approach**: `dp[i]=dp[i>>1]+(i&1)`.  

</details>

<details>
<summary>Happy Number</summary>

- **Pattern**: Cycle detection  
- **Approach**: Sum of squares, detect loop.  

</details>

<details>
<summary>Pow(x,n)</summary>

- **Pattern**: Binary Exponentiation  
- **Approach**: Fast power with squaring.  

</details>

<details>
<summary>Sqrt(x)</summary>

- **Pattern**: Binary Search  
- **Approach**: Find integer root.  

</details>

---

## Stack / Monotonic

<details>
<summary>Next Greater Element I</summary>

- **Pattern**: Monotonic Stack  
- **Approach**: Traverse from right, keep decreasing stack.  

</details>

<details>
<summary>Daily Temperatures</summary>

- **Pattern**: Monotonic Stack  
- **Approach**: Track indices, pop until warmer found.  

</details>

<details>
<summary>Largest Rectangle in Histogram</summary>

- **Pattern**: Monotonic Stack  
- **Approach**: Maintain increasing stack, calculate area.  

</details>

---

## Backtracking / DFS

<details>
<summary>Combination Sum</summary>

- **Pattern**: Backtracking  
- **Approach**: Choose candidate repeatedly or skip.  

</details>

<details>
<summary>Word Search</summary>

- **Pattern**: Backtracking  
- **Approach**: DFS each cell, mark visited.  

</details>

<details>
<summary>Word Search II</summary>

- **Pattern**: Backtracking + Trie  
- **Approach**: DFS with prefix pruning.  

</details>

<details>
<summary>Burst Balloons (H)</summary>

- **Pattern**: Interval DP  
- **Approach**: Pick last balloon inside interval.  

</details>

<details>
<summary>Numbers with Same Consecutive Differences</summary>

- **Pattern**: BFS/DFS generation  
- **Approach**: Build digit by digit with ±k.  

</details>

<details>
<summary>3 Sum / K Sum</summary>

- **Pattern**: Sorting + Two-pointer / Recursion  
- **Approach**: Reduce to 2-sum, recurse.  

</details>

---

## Classic Arrays

<details>
<summary>2 Sum</summary>

- **Pattern**: HashMap  
- **Approach**: Store complement.  

</details>

<details>
<summary>Two Sum II</summary>

- **Pattern**: Two-pointer (sorted)  
- **Approach**: Low/high pointer.  

</details>

---
 -->

# 📘 Last Minute DSA Revision Handbook

| # | Problem Name | Pattern | Speed Revision | Deeper Recall | Complexity | Pointer |
|---|--------------|---------|----------------------------|----------------------------|------------|---------|
| 1 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Sliding Window / Deque | Maintain deque of indices with decreasing values. Front = max. | Use deque to store only useful elements within the window. Pop smaller values from the back, pop out-of-window from front. | O(N), O(K) | Classic sliding window maximum – use deque, not heap. |
| 2 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Greedy / Heap | Arrange tasks with cooldown using max frequency. | Find max frequency task, arrange them first, then fill idle slots with other tasks. Idle = max(0, (maxFreq-1)*(n - countMax)+extra). | O(N), O(1) | Similar to rearrange string problems. |
| 3 | [Single Number](https://leetcode.com/problems/single-number/) | Bit Manipulation | XOR all numbers → unique remains. | XOR cancels pairs since a^a=0, a^0=a. Perfect for finding unique among duplicates. | O(N), O(1) | Watch for variations (3 times, k times → use bit counting). |
| 4 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | DP / Bit Manipulation | dp[i] = dp[i>>1] + (i&1). | Each number’s set bits = previous number’s shifted + LSB. Reuse previous results. | O(N), O(N) | Important for bit-DP, Hamming weight, Gray code. |
| 5 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding Window / HashMap | Expand/shrink window until valid. | Use two pointers. Expand right until covers target, then shrink left to minimize. Maintain count maps. | O(N), O(1) | Watch difference between "minimum substring covering target" vs "longest substring with conditions". |
| 6 | [Regions Cut by Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | Union-Find / DFS | Treat each cell as 4 triangles. | Split each grid cell into 4 subcells, union boundaries. Count connected components. | O(N² α(N)), O(N²) | Very similar to Surrounded Regions / Closed Islands. |
| 7 | [Range Sum Query (Immutable)](https://leetcode.com/problems/range-sum-query-immutable/) | Prefix Sum | Precompute prefix sums. | Prefix[i] = sum up to i. Range query = prefix[r+1]-prefix[l]. | O(1) query, O(N) precompute | Key to range queries. |
| 8 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Monotonic Stack | Traverse nums2, build map of NGE. | Use stack to maintain decreasing sequence. Map each popped element to next greater. Then lookup for nums1. | O(N), O(N) | Monotonic stack template. |
| 9 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers / DP | Use leftMax and rightMax to trap water. | At each index, trapped = min(maxLeft, maxRight) - height[i]. Use prefix/suffix or two pointers. | O(N), O(1) | Very common hard – template for container-based water problems. |
| 10 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary Search | Partition arrays correctly. | Binary search smaller array. Ensure left parts ≤ right parts. Median from max(left) and min(right). | O(log(min(m,n))), O(1) | Template for binary-search partition problems. |
| 11 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | DP Interval | Consider last balloon to burst. | dp[l][r] = max over k in [l,r], dp[l][k-1] + nums[l-1]*nums[k]*nums[r+1] + dp[k+1][r]. | O(N³), O(N²) | Interval DP template (Matrix Chain Multiplication). |
| 12 | [Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) | String | Count spaces, distribute evenly. | Count words and spaces. Spaces between words = totalSpaces/(n-1), remainder at end. | O(N), O(1) | Simple but test parsing carefully. |
| 13 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Interval Tree / BST | Store intervals, check overlap. | Use BST or list. New booking valid if no overlap with neighbors. | O(N), O(N) | Related: My Calendar II, III. |
| 14 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Heap | Maintain min-heap of size k. | Insert new element, pop smallest if >k. Top = kth largest. | O(logK), O(K) | Streaming + heap pattern. |
| 15 | [Gas Station](https://leetcode.com/problems/gas-station/) | Greedy | If total gas < total cost → impossible. | Track total. Restart when tank <0. Start index = current+1. | O(N), O(1) | Greedy template: restart when deficit. |
| 16 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Prefix Sum / HashMap | Track balance count of 0/1. | Convert 0→-1. Keep map of prefix sum. Max length when same balance seen. | O(N), O(N) | Classic "longest subarray with given sum". |
| 17 | [Missing Number](https://leetcode.com/problems/missing-number/) | Bit / Math | Sum formula or XOR. | Either use sum(0..n) - sum(nums), or XOR all. | O(N), O(1) | Watch for overflow, prefer XOR. |
| 18 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie + Backtracking | Build trie, DFS board. | Insert words into trie. DFS each cell, prune by trie prefix. Mark visited. | O(M*4^L), O(W) | Trie pruning is key for optimization. |
| 19 | [Rotten Oranges](https://leetcode.com/problems/rotting-oranges/) | BFS | Multi-source BFS. | Push all rotten oranges at time=0. BFS layer by layer until no fresh left. | O(N*M), O(N*M) | BFS grid template. |
| 20 | [Flood Fill](https://leetcode.com/problems/flood-fill/) | DFS / BFS | Replace color recursively. | From start pixel, DFS all connected same-color cells, change to newColor. | O(N*M), O(N*M) | Classic DFS flood template. |
| 21 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Graph / TopoSort | Detect cycle. | Build graph, use DFS with visited states or Kahn’s BFS. If cycle → false. | O(V+E), O(V+E) | Cycle detection in DAG. |
| 22 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Graph / TopoSort | Return topological order. | Kahn’s algo → BFS queue. Valid order if all nodes processed. | O(V+E), O(V+E) | Same template as Course Schedule. |
| 23 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | DFS / Flood Fill | Flood fill border first. | Mark border-connected lands as water. Then count remaining islands. | O(N*M), O(N*M) | Similar to Surrounded Regions. |
| 24 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | DFS / Flood Fill | Flood fill from border ‘O’. | Any ‘O’ connected to border survives. Rest convert to ‘X’. | O(N*M), O(N*M) | Border-based flood fill. |
| 25 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | BFS | Multi-source BFS from 0s. | Push all 0s, then BFS to update nearest distances for 1s. | O(N*M), O(N*M) | Multi-source BFS template. |
| 26 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS / Graph | BFS from beginWord to endWord. | Precompute neighbors with wildcard dict. BFS levels until found. | O(N*L²), O(N*L) | Bidirectional BFS speeds up. |
| 27 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | BFS / DFS Coloring | Try 2-coloring graph. | Traverse each component, assign colors. Conflict → not bipartite. | O(V+E), O(V) | Template for bipartite checks. |
| 28 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Graph / DFS | Copy nodes + neighbors recursively. | Use hashmap old→new. DFS each neighbor. | O(V+E), O(V) | Always use map to avoid cycles. |
| 29 | [Numbers with Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | BFS / DFS | Generate numbers digit by digit. | Start from 1–9, DFS append next digit if abs diff=k. | O(2^N), O(N) | Backtracking number gen. |
| 30 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | DFS / BFS | Count connected land components. | DFS each land, mark visited. Increment count. | O(N*M), O(N*M) | Classic flood-fill. |
| 31 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | DFS / Union-Find | Count connected components. | Traverse adjacency matrix, mark visited. Or union all connections. | O(N²), O(N) | Graph connectivity template. |
| 32 | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Graph / DFS | DFS/BFS between src & dest. | Simple traversal marking visited. Return true if reached dest. | O(V+E), O(V) | Basic graph connectivity. |
| 33 | [Word Search](https://leetcode.com/problems/word-search/) | Backtracking | DFS search with pruning. | From each cell, DFS neighbors matching word chars. Mark visited. | O(N*M*4^L), O(L) | Key: mark/unmark visited. |
| 34 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS / DFS | BFS rightmost node per level. | Level-order traversal, add last node in queue. | O(N), O(W) | DFS preorder right-first also works. |
| 35 | [LCA of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | DFS | Recursive postorder search. | If node = p/q, return node. If found in both sides, return root. | O(N), O(H) | Template for LCA in trees. |
| 36 | [LCA of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-bst/) | BST / DFS | Exploit BST property. | If both < root, go left. If both > root, go right. Else root = LCA. | O(H), O(1) | BST property simplifies. |
| 37 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | DFS | Check height diff ≤1. | Postorder recursion returning height, -1 if unbalanced. | O(N), O(H) | Early stop when unbalanced. |
| 38 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | DFS | Max path through each node. | Postorder recursion. Update max = leftH+rightH. | O(N), O(H) | Template for longest path. |
| 39 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | DFS | Swap children recursively. | Simple recursion or BFS swap. | O(N), O(H) | Very common warmup. |
| 40 | [Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | BST / Inorder | Inorder traversal → sorted. | Do inorder, count nodes. kth = result. | O(H+k), O(H) | Use stack or recursion. |
| 41 | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) | DFS / Recursion | Check value bounds. | Pass down min/max constraints. Return false if violation. | O(N), O(H) | Important: check ALL nodes. |
| 42 | [Construct BT from Pre/Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Tree Construction / Recursion | Root = preorder[0], split inorder. | Recursively build left/right using indices. Use hashmap for inorder lookup. | O(N), O(N) | Template for tree construction. |
| 43 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Linked List / Two Pointers | Floyd’s cycle detect. | Fast/slow detect cycle. Reset one pointer to head, move both until meet. | O(N), O(1) | Classic cycle detection. |
| 44 | [Middle of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Linked List | Fast/slow pointers. | Slow moves 1 step, fast moves 2. Return slow when fast ends. | O(N), O(1) | Template for linked list. |
| 45 | [Happy Number](https://leetcode.com/problems/happy-number/) | Math / Set | Square-digit sum until loop/1. | Detect cycle using set or Floyd’s cycle. | O(logN), O(1) | Similar to cycle detection. |
| 46 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Monotonic Stack | Store indices of decreasing temps. | For each day, pop until warmer found, record distance. | O(N), O(N) | Stock span variant. |
| 47 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtracking | DFS all combinations. | At each step, choose candidate repeatedly. Track sum. | O(2^N), O(N) | Backtracking template. |
| 48 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap / Divide-Conquer | Min-heap of heads. | Pop min, push next. Or merge pairwise divide-conquer. | O(N logK), O(K) | Similar to k-way merge. |
| 49 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Linked List | Reverse sublist length k. | Traverse groups, reverse links, reconnect. | O(N), O(1) | Careful with pointers. |
| 50 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List / Two Pointers | Detect if cycle. | Floyd’s cycle detection → fast meets slow. | O(N), O(1) | Base for Cycle II. |
| 51 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | String / Two Pointers | Skip non-alphanumeric, compare. | Lowercase letters, move left/right pointers. | O(N), O(1) | Template for string checks. |
| 52 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | String / HashMap | Count pairs of chars. | Use frequency map. Max pairs + 1 if odd leftover. | O(N), O(1) | Palindrome construction basics. |
| 53 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | Push open, pop check close. | Use stack for bracket types. Valid if empty at end. | O(N), O(N) | Parenthesis matching template. |
| 54 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | String / Simulation | Parse string with rules. | Skip spaces, handle +/- sign, digits until invalid. Clamp 32-bit range. | O(N), O(1) | Implementation-heavy. |
| 55 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack | Push nums, pop for ops. | For operator, pop two, apply, push result. | O(N), O(N) | Expression evaluation template. |
| 56 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic Stack | Process bars with stack. | Maintain increasing stack. Compute area when pop. | O(N), O(N) | Stack histogram template. |
| 57 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Sliding Window | At most K zeros. | Expand right, if zero count >k, shrink left. | O(N), O(1) | Template: "longest substring with ≤k". |
| 58 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Move pointers inward. | Left+Right>target → dec right, else inc left. | O(N), O(1) | Sorted array trick. |
| 59 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Linked List / Math | Simulate digit addition. | Traverse both, track carry. Append nodes. | O(N), O(N) | Classic linked list + carry. |
| 60 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Design / HashMap+DLL | HashMap + doubly-linked list. | Map key→node. DLL maintains LRU order. | O(1) ops, O(Capacity) | Standard design Q. |
| 61 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window + HashMap | Track chars with sliding window. | Expand window until duplicate; shrink from left; maintain max length. | O(n), O(k) | Core sliding window template. |
| 62 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Two Pointers | Max area by shrinking width smartly. | Use two pointers from ends, move smaller height inward, track max area. | O(n), O(1) | Standard two-pointer trick. |
| 63 | [Two Sum](https://leetcode.com/problems/two-sum/) | HashMap | Store complement while iterating. | Iterate, if target-num exists in map, return indices; else store num. | O(n), O(n) | Classic hashmap usage. |
| 64 | [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers + Sorting | Sort + fix one + 2Sum. | Sort array, fix one element, use two pointers for the rest, skip duplicates. | O(n²), O(1) | Template extends to 4Sum/KSum. |
| 65 | [K Sum](https://leetcode.com/problems/4sum/) | Recursion + Two Pointers | Reduce K to 2. | Sort, recursively reduce K until 2Sum, solve using two pointers. | O(n^(k-1)), O(k) | Generic k-sum approach. |
| 66 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hashing | Group by char counts. | Use sorted string or char count tuple as hashmap key, group words. | O(n*k log k), O(nk) | Sorting vs counting method. |
| 67 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Heap/Bucket Sort | Count + pick top k. | Use hashmap to count freq, then min-heap or bucket sort to get top k. | O(n log k) or O(n), O(n) | Bucket sort is neat optimization. |
| 68 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Prefix Sum + HashMap | Store prefix sum counts. | Use running sum, store how many times (sum-k) appeared; accumulate counts. | O(n), O(n) | Foundation for many prefix-sum problems. |
| 69 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Sorting/HashMap | Compare char counts. | Either sort both strings or compare hashmap counts. | O(n log n) / O(n), O(1) | Edge cases: unicode/large alphabets. |
| 70 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | Use set for unique chars. | Slide window, track seen chars, remove duplicates by shrinking left. | O(n), O(k) | One of the most repeated sliding window patterns. |
| 71 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Two Pointers | Maximize width × min height. | Start with farthest pointers, move inward from shorter line; maximize water. | O(n), O(1) | Always move shorter pointer. |
| 72 | [2 Sum](https://leetcode.com/problems/two-sum/) | HashMap | Store needed value. | Iterate once, check if target-num in map, else store. | O(n), O(n) | Good warmup. |
| 73 | [3 Sum](https://leetcode.com/problems/3sum/) | Sorting + Two Pointers | Fix one, 2Sum for rest. | After sorting, skip duplicates, run two pointers for pairs. | O(n²), O(1) | Generalizes to K-sum. |
| 74 | [K Sum](https://leetcode.com/problems/4sum/) | Recursion + 2Sum | Recursive reduction. | Solve recursively until 2-sum base, use two pointers. | O(n^(k-1)), O(k) | Careful with duplicates. |
| 75 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic Stack | Track heights with stack. | Push increasing heights, pop when smaller height comes, compute area. | O(n), O(n) | Core monotonic stack template. |
| 76             | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Sliding Window + HashMap       | Count subarrays with **at most K distinct** - Count subarrays with **at most (K-1) distinct** → difference = exact K | Use the "at most K" trick with sliding window and hashmaps. Maintain frequency counts of elements. The number of subarrays with exactly K = (subarrays with at most K) – (subarrays with at most (K-1)). This reduces complexity drastically. | Time: O(n), Space: O(n)            | Classic trick: exact K = atMost(K) – atMost(K-1). Same trick applies to problems with “exactly K” constraints.       |
| 77             | [Subarrays with atmost K Different Integers](https://leetcode.com/discuss/post/1622358/uber-oa-find-subarrays-with-at-least-k-u-2yp0/) | Sliding Window + HashMap       | Total Sub arrays **(n * (n+1))//2** - Count subarrays with **at most (K-1) distinct** → difference = atmost K | Use the "at most K" trick with sliding window and hashmaps. Maintain frequency counts of elements. The number of subarrays with exactly K = (subarrays with at most K) – (subarrays with at most (K-1)). This reduces complexity drastically. | Time: O(n), Space: O(n)            | Classic trick: exact K = atMost(K) – atMost(K-1). Same trick applies to problems with “exactly K” constraints.       |
