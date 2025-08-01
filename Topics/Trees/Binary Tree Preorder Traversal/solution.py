# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def preorder(root: Optional[TreeNode]):
        if not root:
            return

        result.append(root.val)
        preorder(root.left)
        preorder(root.right)
    
    preorder(root)
    return result
    

# Test Case:
root = [1,2,3,4,5,None,8,None,None,6,7,9]
output = [1,2,4,5,6,7,3,8,9]

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
result = preorderTraversal(root_node)
print("Result:", result)
print("Passes Test:", result == output)