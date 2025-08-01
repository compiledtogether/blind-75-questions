# https://leetcode.com/problems/invert-binary-tree

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    ## Recursive Approach
    # if not root:
    #     return

    # temp = root.left
    # root.left = root.right
    # root.right = temp

    # invertTree(root.left)
    # invertTree(root.right)

    # return root

    ## Deque Approach
    if not root: return root
    q = deque([root])

    while q:
        node = q.popleft()
        
        node.left, node.right = node.right, node.left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return root
        
# Test Case:

root = [4,2,7,1,3,6,9]
output = [4,7,2,9,6,3,1]

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

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left) # type: ignore
            queue.append(node.right) # type: ignore
        else:
            result.append(None)

    # Trim trailing None values (not needed for structure)
    while result and result[-1] is None:
        result.pop()

    return result

root_node = build_tree(root) # type: ignore
result = invertTree(root_node)
print("Passes Test:", tree_to_list(result) == output)