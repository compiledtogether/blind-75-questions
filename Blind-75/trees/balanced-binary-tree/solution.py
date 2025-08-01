# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return True, 0  # isBalanced, height

        left_balanced, left_height = dfs(node.left)
        right_balanced, right_height = dfs(node.right)

        isBalanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return isBalanced, 1 + max(left_height, right_height)

    return dfs(root)[0]

        
# Test Case:

root = [3,9,20,None,None,15,7]
output = True

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

root_node = build_tree(root) # type: ignore
result = isBalanced(root_node)
print("Passes Test:", result == output)