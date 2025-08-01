# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result, queue, reverse = [], deque([root]), False
    if not root: return result

    while queue:
        level = []
        for _ in range(len(queue)):
            if not reverse:
                node = queue.popleft()
                level.append(node.val) # type: ignore
                if node.left: queue.append(node.left) # type: ignore
                if node.right: queue.append(node.right) # type: ignore
            else:
                node = queue.pop()
                level.append(node.val) # type: ignore
                if node.right: queue.appendleft(node.right) # type: ignore
                if node.left: queue.appendleft(node.left) # type: ignore
            
        result.append(level)
        reverse = not reverse

    return result

# Test Case:
root = [3,9,20,None,None,15,7]
output = [[3],[20,9],[15,7]]

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
result = zigzagLevelOrder(root_node)
print("Result:", result)
print("Passes Test:", result == output)

        