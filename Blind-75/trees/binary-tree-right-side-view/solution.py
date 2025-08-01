# https://leetcode.com/problems/binary-tree-right-side-view
from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    result, queue = [], deque([root])

    while queue:
        rightSide = None

        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                rightSide = node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
        if rightSide:
            result.append(rightSide.val)

    return result
        

# Test Case:

root = [1,2,3,None,5,None,4]
output = [1,3,4]

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
result = rightSideView(root_node)
print("Result:", result)
print("Passes Test:", result == output)