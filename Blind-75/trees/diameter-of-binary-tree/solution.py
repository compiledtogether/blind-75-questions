# https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0, 0  # height, diameter

        left_height, left_diameter = dfs(node.left)
        right_height, right_diameter = dfs(node.right)

        # current height
        height = 1 + max(left_height, right_height)
        # diameter through current node
        diameter_through_root = left_height + right_height
        # max diameter so far
        diameter = max(left_diameter, right_diameter, diameter_through_root)

        return height, diameter

    return dfs(root)[1]

# Test Case:

root = [1,2,3,4,5]
output = 3

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
result = diameterOfBinaryTree(root_node)
print("Result:", result)
print("Passes Test:", result == output)