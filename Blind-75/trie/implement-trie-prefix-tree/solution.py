# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    
    def _traverse(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]

        return node
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Test Cases:

trie = Trie()
trie.insert("apple")
print(trie.search("apple") == True)
print(trie.search("app") == False)
print(trie.startsWith("app") == True)
trie.insert("app")
print(trie.search("app") == True)