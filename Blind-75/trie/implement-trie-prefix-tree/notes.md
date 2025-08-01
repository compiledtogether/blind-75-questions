# Implement Trie (Prefix Tree)

## Topics
- Trie
- Hashing
- Design

---

## Explanation

A **Trie (Prefix Tree)** is a tree-based data structure used for efficient retrieval of keys in datasets of strings. Each node in the Trie represents a character of the input strings.

### Key Concepts:
- Each node has a dictionary `children` mapping characters to the next `TrieNode`.
- `is_end` flag marks the end of a word.
- Used for operations like autocomplete, spell checking, and dictionary word search.

---

## Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}     # maps character to TrieNode
        self.is_end = False    # True if this node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()
```

## Operations

### Insert

```python
def insert(self, word: str) -> None:
    node = self.root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.is_end = True
```

Purpose: Add a word to the Trie.

Time Complexity: O(n), where n = length of the word.


### Search

```python
def search(self, word: str) -> bool:
    node = self._traverse(word)
    return node is not None and node.is_end
```

Purpose: Check if the word exists in the Trie.

Time Complexity: O(n), where n = length of the word.


### startsWith

```python
def startsWith(self, prefix: str) -> bool:
    return self._traverse(prefix) is not None
```

Purpose: Check if there is any word in the Trie that starts with the given prefix.

Time Complexity: O(p), where p = length of the prefix.

### Traverse (Helper)

```python
def _traverse(self, word):
    node = self.root
    for ch in word:
        if ch not in node.children:
            return None
        node = node.children[ch]
    return node
```

Used internally by search and startsWith to traverse the Trie.

---

## Test Cases

**Input**
trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app")
assert trie.search("app") == True
**Output**
output = True

---

## Time & Space Complexity

1. Insert

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(h)      |

1. Search

| Complexity | Value     |
|------------|-----------|
| Time       | O(n)      |
| Space      | O(1)      |

1. StartsWith

| Complexity | Value     |
|------------|-----------|
| Time       | O(p)      |
| Space      | O(1)      |

where p = length of the prefix.

---