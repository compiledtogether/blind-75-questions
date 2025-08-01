# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    ## only recursive and slicing
    # if not preorder or not inorder:
    #     return None
    
    # root = TreeNode(preorder[0]) # first item in preorder will be root
    # mid = inorder.index(preorder[0]) # root index

    # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

    # return root

    ## Using recursion and Hashmap
    idx_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0
    
    def helper(in_left: int, in_right: int):
        nonlocal pre_idx # use the global pre_idx
        if in_left > in_right:
            return None
        
        root = TreeNode(preorder[pre_idx])             # type: ignore
        index = idx_map[preorder[pre_idx]] # type: ignore
        pre_idx += 1 # type: ignore

        root.left = helper(in_left, index - 1)
        root.right = helper(index + 1, in_right)
        return root
    
    return helper(0, len(inorder) - 1)
    
# Test Case:

preorder = [3,9,20,15,7] 
inorder = [9,3,15,20,7]
output = [3,9,20,None,None,15,7]

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


result = buildTree(preorder, inorder)
print("Passes Test:", tree_to_list(result) == output) # type: ignore