# https://leetcode.com/problems/minimum-depth-of-binary-tree

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if not root: return 0

    if root.left is None: return 1 + minDepth(root.right)
    if root.right is None: return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))
        
# Test Case:

root = [3,9,20,None,None,15,7]
output = 2

# Helper function to build tree from level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()
        if values[index] is not None:
            node.left = TreeNode(values[index]) # type: ignore
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index]) # type: ignore
            queue.append(node.right)
        index += 1

    return root

root_node = build_tree(root)
result = minDepth(root_node)
print("Result:", result)
print("Passes Test:", result == output)