# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root # type: ignore

    left = lowestCommonAncestor(root.left, p, q) # type: ignore
    right = lowestCommonAncestor(root.right, p, q) # type: ignore

    return root if left and right else left or right
        

# Test Case:

root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8
output = 6

# Helper function to build tree from level-order list
def build_tree(values):
    """Builds a binary search tree from a list using level-order insertion."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index]) # type: ignore
            queue.append(node.left) # type: ignore
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index]) # type: ignore
            queue.append(node.right) # type: ignore
        index += 1

    return root

def find_node(root, val):
    """Find a node in the tree with a specific value."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

# Test Example
values = [6,2,8,0,4,7,9,None,None,3,5]
root = build_tree(values)
p = find_node(root, 2)
q = find_node(root, 8)

lca = lowestCommonAncestor(root, p, q) # type: ignore
print("LCA:", lca.val)  # Output should be 6
print("Passes Test:", lca.val == output)

